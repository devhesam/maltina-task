from django.utils.translation import gettext_lazy as _

""" Success message codes: Range [2000 - 2999] """
SUCCESS_USER_ACCOUNT_CHECK_PERMISSION = 2000


SUCCESS_MESSAGE_CODES = {
    SUCCESS_USER_ACCOUNT_CHECK_PERMISSION: _("User account check permission is successfully"),
}

""" Error message codes: Range [4000 - 4999] """
ERROR_UNKNOWN = 4000
ERROR_INVALID_AUTHORIZATION_HEADER = 4001

ERROR_MESSAGE_CODES = {
    ERROR_INVALID_AUTHORIZATION_HEADER: _("Invalid authorization header. No credentials provided."),

}

""" All message codes are merged together in this section """
MESSAGE_CODES = {**SUCCESS_MESSAGE_CODES, **ERROR_MESSAGE_CODES}
