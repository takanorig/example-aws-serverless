import logging

from aws_xray_sdk.core import patch_all

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

patch_all()


def post_confirmation_handler(event, context):
    user_attrs = _get_user_attributes(event)
    if not user_attrs:
        return event

    trigger_source = event.get('triggerSource')
    if trigger_source == 'PostConfirmation_ConfirmSignUp':
        logger.info('User signed up. : user=%s', user_attrs)

    return event


def post_authentication_handler(event, context):
    user_attrs = _get_user_attributes(event)
    if not user_attrs:
        return event

    logger.info('User authenticated. : user=%s', user_attrs)

    return event


def _get_user_attributes(event):
    request = event.get('request')
    if not request:
        logger.warning('Not found the trigger request. event=%s', event)
        return None

    user_attrs = request.get('userAttributes')
    if not user_attrs:
        logger.warning('Not found the Cognito User Attributes. event=%s', event)
        return None

    return user_attrs
