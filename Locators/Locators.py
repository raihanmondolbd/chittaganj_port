from selenium.webdriver.common.by import By


class Locators:
    detailsFirst = By.XPATH, '(//span[contains(text(), "Details")])[1]'
    viewIcon = By.XPATH, '//tbody/tr/td[last()]/a/i'
    applyNowButton = By.XPATH, '//strong'
    continueWithoutLogin = By.XPATH, '//a[contains(text(),"Continue without Login")]'
    nidTextField = By.XPATH, '//input[@id="national_id"]'
    nidAttachment = By.XPATH, '//input[@id="national_id_attachment"]'
    dateOfBirth = By.XPATH, '//input[@id="date_of_birth"]'
    dateOfBirthClass = By.CLASS_NAME, "datetimepicker-input"
    selectMonth = By.XPATH, "//th[@title='Select Month']"
    previusMonth = By.XPATH, "//span[@title='Previous Month']"
    date_23 = By.XPATH, "//td[normalize-space()='23']"
    nidVerification = By.ID, 'nid_verification'

    fatherName = By.ID, 'father_name'
    motherName = By.ID, 'mother_name'
    mobileNumber = By.ID, 'mobile'
    otpNumber = By.ID, 'otp'
    email = By.ID, 'email'
    religion = By.ID, 'religion'
    photo = 'photo'
    signature = 'signature'
    nextButton = By.XPATH, '// button[contains(text(), "Next") and @value="first"]'

    permanent_division = By.ID, 'permanent_division'
    permanent_district = By.ID, 'permanent_district'
    permanent_thana = By.ID, 'permanent_thana'
    permanent_post_office_name = By.ID, 'permanent_post_office_name'
    permanent_post_code = By.ID, 'permanent_post_code'
    permanent_address = By.ID, 'permanent_address'

    present_division = By.ID, 'present_division'
    present_district = By.ID, 'present_district'
    present_thana = By.ID, 'present_thana'
    present_post_office_name = By.ID, 'present_post_office_name'
    present_post_code = By.ID, 'present_post_code'
    present_address = By.ID, 'present_address'
    nextButton2 = By.XPATH, '(// button[contains(text(), "Next")])[2]'

    education_0_exam = By.ID, 'education_0_exam'
    education_0_subject = By.ID, 'education_0_subject'
    education_0_exam_body = By.ID, 'education_0_exam_body'
    education_0_passing_year = By.ID, 'education_0_passing_year'
    education_0_result_type = By.ID, 'education_0_result_type'
    education_0_result = By.ID, 'education_0_result'

    education_1_exam = By.ID, 'education_1_exam'
    education_1_subject = By.ID, 'education_1_subject'
    education_1_exam_body = By.ID, 'education_1_exam_body'
    education_1_passing_year = By.ID, 'education_1_passing_year'
    education_1_result_type = By.ID, 'education_1_result_type'
    education_1_result = By.ID, 'education_1_result'
    nextButton3 = By.XPATH, '(// button[contains(text(), "Next")])[3]'
