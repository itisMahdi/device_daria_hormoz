LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)
LOCAL_MODULE := android.hardware.vibrator-service.hormoz
LOCAL_VINTF_FRAGMENTS := android.hardware.vibrator.hormoz.xml
LOCAL_INIT_RC := vibrator-hormoz.rc
LOCAL_VENDOR_MODULE := true
LOCAL_MODULE_RELATIVE_PATH := hw

LOCAL_SRC_FILES := \
    Vibrator.cpp \
    VibratorUtils.cpp \
    main.cpp

LOCAL_SHARED_LIBRARIES := \
    libbase \
    libbinder_ndk \
    android.hardware.vibrator-V2-ndk

include $(BUILD_EXECUTABLE)
