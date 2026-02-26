#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2025 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (  # pyright: ignore
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (  # pyright: ignore
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {
    'vendor/lib64/libwifi-hal-mtk.so': blob_fixup().fix_soname(),
    'vendor/lib64/hw/hwcomposer.mt6877.so': blob_fixup().binary_regex_replace(
        b'OnScreenFingerprintDimLayer', b'SurfaceView[UdfpsController/'
    ),
    'system_ext/lib64/libsource.so': blob_fixup().add_needed('libui_shim.so'),
    (
        'vendor/bin/hw/vendor.mediatek.hardware.mtkpower@1.0-service',
        'vendor/lib64/android.hardware.power-service-mediatek.so',
    ): blob_fixup().replace_needed(
        'android.hardware.power-V2-ndk_platform.so',
        'android.hardware.power-V2-ndk.so'
    ),
    (
        'vendor/bin/hw/android.hardware.gnss-service.mediatek',
        'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so',
    ): blob_fixup().replace_needed(
        'android.hardware.gnss-V1-ndk_platform.so',
        'android.hardware.gnss-V1-ndk.so'
    ),
    (
        'vendor/lib*/hw/vendor.mediatek.hardware.pq@2.15-impl.so',
        'vendor/lib64/libmtkcam_stdutils.so',
        'vendor/lib64/hw/android.hardware.camera.provider@2.6-impl-mediatek.so',
    ): blob_fixup().replace_needed('libutils.so', 'libutils-v32.so'),
    (
        'vendor/lib64/libwvhidl.so',
        'vendor/lib64/mediadrm/libwvdrmengine.so'
    ): blob_fixup().replace_needed(
        'libprotobuf-cpp-lite-3.9.1.so', 'libprotobuf-cpp-full-3.9.1.so'
    ),
    (
        'vendor/bin/mnld', 'vendor/lib64/libcam.utils.sensorprovider.so'
    ): blob_fixup().replace_needed(
        'libsensorndkbridge.so', 'libsensorndkbridge-v30.so'
    ),
    'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek': blob_fixup()
    .add_needed(
        'libstagefright_foundation-v33.so'
    ),
    'vendor/bin/hw/mtkfusionrild': blob_fixup().add_needed('libutils-v32.so'),
}

module = ExtractUtilsModule(
    'hormoz',
    'daria',
    blob_fixups=blob_fixups,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
