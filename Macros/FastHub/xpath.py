# this file use  for constant tag define by XPATH
USERNAME = "theautomationtester"
PASSWORD = "NQyZJdt27afj"

BASIC_AUTHENTICATION_SIGNIN_TEXTVIEW = "//android.widget.TextView[@resource-id='com.fastaccess.github:id/basicAuth']"
BASIC_AUTHENTICATION_SIGNIN_USERNAME_FIELD = "//android.widget.EditText[@resource-id='com.fastaccess.github:id/usernameEditText']"
BASIC_AUTHENTICATION_SIGNIN_PASSWORD_FIELD = "//android.widget.EditText[@resource-id='com.fastaccess.github:id/passwordEditText']"
BASIC_AUTHENTICATION_SIGNIN_SIGNIN_BUTTON = "//android.widget.ImageButton[@resource-id='com.fastaccess.github:id/login']"
BASIC_AUTHENTICATION_SIGNIN_PROGRESS_BAR = "//android.widget.ProgressBar[@resource-id='com.fastaccess.github:id/progress']"

MAIN_DRAWER_NAVIGATION_UP = "//android.widget.ImageButton[@content-desc='Navigate up']"
MAIN_DRAWER_NAVIGATION_UP_23 = "//android.view.ViewGroup[@resource-id='com.fastaccess.github:id/toolbar']//android.widget.ImageButton"
MAIN_TEXTVIEW_TOOLBAR = "//android.widget.TextView[@text='FastHub']"
DRAWER_PROFILE_TAB = "//*[@content-desc='Profile']"
DRAWER_PROFILE_LOGOUT = "//android.widget.FrameLayout[@resource-id='com.fastaccess.github:id/logout']"
LOGOUT_DIALOG = "//android.widget.TextView[@resource-id='com.fastaccess.github:id/message']"
LOGOUT_DIALOG_YES = "//android.widget.Button[@resource-id='com.fastaccess.github:id/ok']"

MAIN_TAB_ISSUES = "//android.view.View[@resource-id='com.fastaccess.github:id/pinned']"
ISSUES_RECYCLER_CHILDS = "//*[@resource-id='com.fastaccess.github:id/recycler']//android.widget.RelativeLayout"
ISSUE_TEXTVIEW = "//android.widget.TextView[@resource-id='com.fastaccess.github:id/details' and contains(text(), 'cafebazaar/AdContainer#1')]"
ISSUE_TITLE_EDIT_SECTION = "//android.widget.TextView[@text='AdContainer']"
ISSUE_CAREATED_TEXTVIEW = "//*[contains(text(), 'Created')]"
ISSUE_SUBJECT_EXTRACT = "//android.widget.TextView[@resource-id='com.fastaccess.github:id/title']"
ISSUE_DESCRIPTION_EXTRACT = "//android.widget.TextView[@resource-id='com.fastaccess.github:id/details']"
COMMENT_MENU = "//android.widget.ImageView[@resource-id='com.fastaccess.github:id/commentMenu']"
COMMENT_MENU_EDIT = "//android.widget.TextView[@resource-id='android:id/title' and @text='Edit']"
UPDATE_ISSUE_TEXTVIEW = "//android.widget.TextView[@text='Update Issue']"

UPDATE_ISSUE_TITLE = "//android.widget.LinearLayout[@resource-id='com.fastaccess.github:id/title']//android.widget.EditText"
UPDATE_ISSUE_DESCRIPTION_BUTTON = "//android.widget.TextView[@resource-id='com.fastaccess.github:id/description']"
UPDATE_ISSUE_SUBMIT_BUTTON = "//android.widget.ImageButton[@resource-id='com.fastaccess.github:id/submit']"

DESCRIPTION_MARKDOWN = "//android.widget.TextView[@text='Markdown']"
DESCRIPTION_EDITTEXT = "//android.widget.EditText[@resource-id='com.fastaccess.github:id/editText']"
DESCRIPTION_SUBMIT = "//android.widget.TextView[@resource-id='com.fastaccess.github:id/submit']"

DESCRIPTION_ASSERT = "//android.widget.TextView[@resource-id='com.fastaccess.github:id/comment']"
DESCRIPTION_HEADER_TITLE = "//android.widget.TextView[@resource-id='com.fastaccess.github:id/headerTitle']"

NAVIGATION_UP = "//android.widget.ImageButton[@content-desc='Navigate up']"
CHANGELOG = "//android.widget.TextView[@text='Changelog']"
