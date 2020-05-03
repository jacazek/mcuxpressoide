Summary: Segger jlink

%define version 6.624

Name: jlink
URL: https://www.segger.com
Version: %{version}
Release: 1
License: GPL
Requires: libncurses5
Requires: glibc
BuildRoot: ~/DEV/installer/rpmbuild/tmp/jlink/

%description
SEGGER J-Link tools
This package provides software tools
for SEGGER J-Link debug probes.



%prep
echo "BUILDROOT = $RPM_BUILD_ROOT"
cp -R /home/jacob/DEV/installer/JLink_Linux_x86_64/data/ $RPM_BUILD_ROOT/

%files
%attr(0644,root,users) %config /etc/udev/rules.d/99-jlink.rules
/opt/SEGGER/JLink
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkRTTLoggerExe
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Doc/LicenseIncGUI.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Doc/UM08001_JLink.pdf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Doc/ReleaseNotes/ReleaseNotes_JLink.html
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/libQtCore.so
/opt/SEGGER/JLink_V662d/libQtCore.so
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/libQtGui.so.4.8.7
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JFlashLiteExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkGDBServerExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/libQtCore.so.4
/opt/SEGGER/JLink_V662d/libQtCore.so.4
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkSWOViewerExe
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/JLinkDevices.xml
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/RTT/SEGGER_RTT_V662d.tgz
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/gdb/gdbinit/gdbinit_template.jlink
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/gdb/gdbinit/gdbconnectwiem.jlink
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/gdb/gdbinit/gdbconnectem.jlink
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/gdb/gdbinit/gdbconnectsp.jlink
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/gdb/gdbinit/gdbns9xxx.jlink
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/gdb/gdbinit/gdbconnect50.jlink
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/gdb/gdbinit/gdbconnectme.jlink
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/gdb/gdbinit/gdbns7520.jlink
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/gdb/gdbinit/gdbrom.jlink
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/gdb/gdbinit/gdbnet50.jlink
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/gdb/gdbinit/gdbconnectwime.jlink
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/gdb/gdbinit/LPC1768_RAM.jlink
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/JLink/Scripts/Template_ExcludeIllegalRegions.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/JLink/Scripts/Broadcom_BCM53014.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/JLink/Scripts/FujitsuMB86R11EVB.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/JLink/Scripts/Renesas_RZG1M_ConnectCore1.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/JLink/Scripts/Renesas_RZG1M_ConnectCore0.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/JLink/Scripts/Renesas_RZG1E_ConnectCore1.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/JLink/Scripts/iMX23.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/JLink/Scripts/DigiConnectCoreWi-iMX51.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/JLink/Scripts/CogentCSB740Board_OMAP3550.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/JLink/Scripts/ScriptBeagleBoard_OMAP3530.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/JLink/Scripts/Renesas_RZG1E_ConnectCore0.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Samples/JLink/SettingsFiles/Sample.jlinksettings
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/libjlinkarm.so
/opt/SEGGER/JLink_V662d/libjlinkarm.so
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkRTTLogger
/opt/SEGGER/JLink_V662d/JLinkRTTLogger
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkGDBServer
/opt/SEGGER/JLink_V662d/JLinkGDBServer
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/libjlinkarm_x86.so.6
/opt/SEGGER/JLink_V662d/libjlinkarm_x86.so.6
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkSTM32
/opt/SEGGER/JLink_V662d/JLinkSTM32
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JFlashSPICLExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkRTTClient
/opt/SEGGER/JLink_V662d/JLinkRTTClient
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JMemExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/libjlinkarm.so.6.62.4
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/libQtGui.so
/opt/SEGGER/JLink_V662d/libQtGui.so
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkRTTClientExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkConfigExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkRemoteServer
/opt/SEGGER/JLink_V662d/JLinkRemoteServer
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JTAGLoadExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkLicenseManagerExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkSTM32Exe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkGUIServerExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkRegistration
/opt/SEGGER/JLink_V662d/JLinkRegistration
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkRemoteServerCLExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JRunExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/libjlinkarm.so.6
/opt/SEGGER/JLink_V662d/libjlinkarm.so.6
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/GDBServer/RTOSPlugin_FreeRTOS.so
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/GDBServer/RTOSPlugin_embOS.so
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/GDBServer/RTOSPlugin_ChibiOS.so
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/GDBServer/Readme_RTOSPluginChibiOS.txt
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/x86/libjlinkarm.so
/opt/SEGGER/JLink_V662d/x86/libjlinkarm.so
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/x86/libjlinkarm.so.6.62.4
/opt/SEGGER/JLink_V662d/x86/libjlinkarm.so.6.62.4
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/x86/libjlinkarm.so.6
/opt/SEGGER/JLink_V662d/x86/libjlinkarm.so.6
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkGDBServerCLExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/ThirdParty/libedit.so.0.0.47
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/ThirdParty/libedit.so.0
/opt/SEGGER/JLink_V662d/ThirdParty/libedit.so.0
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/ThirdParty/ThirdPartyLicense.txt
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/libjlinkarm_x86.so.6.62.4
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkRTTViewerExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkLicenseManager
/opt/SEGGER/JLink_V662d/JLinkLicenseManager
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/libQtCore.so.4.8.7
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/libQtGui.so.4
/opt/SEGGER/JLink_V662d/libQtGui.so.4
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JFlashSPI_CL
/opt/SEGGER/JLink_V662d/JFlashSPI_CL
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkRemoteServerExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/libQtGui.so.4.8
/opt/SEGGER/JLink_V662d/libQtGui.so.4.8
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/libQtCore.so.4.8
/opt/SEGGER/JLink_V662d/libQtCore.so.4.8
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkSWOViewer
/opt/SEGGER/JLink_V662d/JLinkSWOViewer
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Maxim/MAX32600/MAX32600.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Microchip/MEC1501/Microchip_MEC1501_EvergladesEVB_QSPI_ES.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Microchip/PIC32CX/Microchip_PIC32CX0525SG12xxx_EvergladesEVB_QSPI_ES.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Microchip/CEC1702/Microchip_CEC1702_Clicker_QSPI_ES.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ST/STM32F7/ST_STM32F723I_Disco_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ST/STM32F7/Readme.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ST/STM32F7/ST_STM32F746G_Disco_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ST/STM32H7/ST_STM32H7xx.pex
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ST/STM32H7/ST_STM32H753_Eval_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ST/STM32H7/ST_STM32H745I_Disco_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ST/STM32F4/ST_STM32F413H_Disco_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ST/STM32F4/ST_STM32F412G_Disco_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ST/STM32F4/Readme.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ST/STM32F4/ST_STM32F469I_Disco_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ST/STM32L4/ST_STM32L496G_Disco_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ST/STM32L4/Readme.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ST/STM32L4/ST_STM32L4R9I_Disco_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ST/STM32L4/ST_STM32L476G_Disco_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/AnalogDevices/Readme.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/AnalogDevices/ADSP-CM41/CM41x_FlashB_512.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/AnalogDevices/ADSP-CM41/CM41x_FlashB_256.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/AnalogDevices/ADSP-CM41/CM41x_FlashA_1024.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/AnalogDevices/ADSP-CM41/CM41x_FlashA_256.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/AnalogDevices/ADSP-CM41/Analog_CM41x_M4.pex
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/AnalogDevices/ADSP-CM41/CM41x_FlashA_512.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/AnalogDevices/ADSP-CM41/CM41x_FlashB_128.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/AnalogDevices/ADSP-CM41/CM41x_FlashA_128.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/AnalogDevices/ADuCM410/ADuCM410.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/AnalogDevices/ADuCM410/AnalogDevices_ADuCM410.pex
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/AnalogDevices/ADUCM4x50/ADuCM4x50.axf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ONSemiconductor/RSL10/ONSemiconductor_RSL10.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ONSemiconductor/RSL10/Readme_ONSemiconductor.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ONSemiconductor/RSL10/ONSemiconductor_RSL10_Main_Flash.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ONSemiconductor/RSL10/ONSemiconductor_RSL10_NVR_Flash.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ClouderSemi/CR600/Readme.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ClouderSemi/CR600/CR600.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ClouderSemi/CR600/CR600.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Samsung/Readme.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Samsung/ARTIK05X.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Broadcom/BCM43907.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Zilog/Z32F0642/Z32F0642.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Zilog/Z32F0642/Readme_Zilog.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Renesas/RZ_A2M/Renesas_RZ_A2M_OctaFlash.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Renesas/RZ_A2M/Renesas_RZ_A2M_HyperFlash.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Renesas/RZ_A2M/Renesas_RZ_A2M_QSPI_HyperFlash.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Renesas/RZN1/Renesas_RZN1_Cortex-A7_CPU0.pex
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Renesas/RZN1/Renesas_RZN1_Cortex-M3.pex
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Renesas/RZN1/Renesas_RZN1_Cortex-A7_CPU1.pex
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/Readme.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE984x/TLE9843_2_EEP.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE984x/TLE9844_2_EEP.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE984x/TLE9844_EEP.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE984x/TLE984x_OPT.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE984x/TLE9842_2_EEP.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE984x/TLE9843_EEP.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE984x/TLE9845_EEP.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE984x/TLE9842_EEP.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE985x/TLE9850.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE985x/TLE9851_EEP.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE985x/TLE9854_EEP.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE985x/TLE9852.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE985x/TLE9854.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE985x/TLE9853.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE985x/TLE9852_EEP.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE985x/TLE9853_EEP.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE985x/TLE9851.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE985x/Infineon_TLExxx.pex
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE985x/TLE9850_EEP.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE985x/TLE985x_OPT.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE985x/TLE9855_EEP.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Infineon/TLE985x/TLE9855.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Nuvoton/Nuvoton_NuMicro_M2351.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/SiFive/SiFive_FE310_ARTYBoard_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/SiFive/SiFive_FE310.pex
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/CYW43907/CYW4390x_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/Cypress_S6J328.pex
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xx6.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xx7.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxA_SFLASH_PKEY.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxA_CM0p.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxx_SFLASH_NAR.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxA_sect256KB.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/Readme_Cypress.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxx_SFLASH_USER.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxx_SMIF.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xx5_sect256KB.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxA_SMIF.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xx6_sect256KB.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxA_CM0p_tm_xx.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxA_WFLASH.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxx_CM0p_tm_xA.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxx_WFLASH.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxA_CM4.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xx7_CM0p_tm_xx.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xx7_CM4.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xx7_sect256KB.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxx_SFLASH.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxA_SFLASH.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/version.dat
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxA_SFLASH_NAR.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxx_SFLASH_TOC2.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxA_CM0p_tm_xA.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxA.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxx_CM0p_tm_xx.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxA_CM0p_tm.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxx_EFUSE.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xx7_CM0p_tm_xA.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxx_CM0p.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xx7_CM0p.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxx_SFLASH_PKEY.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxA_SFLASH_TOC2.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxx_CM4.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xx5.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxA_EFUSE.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC6/CY8C6xxA_SFLASH_USER.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/Cypress/PSoC5/Cypress_PSoc5_EEPROM.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX7D/NXP_iMX7D_Connect_CortexM4.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX7D/NXP_iMX7D_SABRE_Board_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX7D/NXP_iMX7D_Connect_CortexA7_0.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX7D/NXP_iMX7D_Connect_CortexA7_1.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX6SX/NXP_iMX6SX_SABRE_Board_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX6SX/iMX6SX_CortexM4.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX6SX/iMX6SX_CortexA9.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMXRT102x/NXP_iMXRT102x_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMXRT105x/NXP_iMXRT105x.pex
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMXRT105x/NXP_iMXRT105x_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMXRT105x/NXP_iMXRT105x_HyperFlash.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX8M/Readme_NXP.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX8M/NXP_iMX8M_Connect_CortexM4.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMXRT101x/NXP_iMXRT1010_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMXRT101x/NXP_iMXRT101x_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX8MM/Readme_NXP.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX8MM/NXP_iMX8M_Connect_CortexM4.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX6UL/NXP_iMX6UL_EVK_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX6UL/NXP_iMX6ULL.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX8MN/Readme_NXP.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX8MN/NXP_iMX8M_Connect_CortexM7.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX8QX/NXP_iMX8QX_Connect_CortexM4.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX8QX/Readme_NXP.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX8QM/Readme_NXP.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX8QM/NXP_iMX8QM_Connect_CortexM4_0.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX8QM/NXP_iMX8QM_Connect_CortexM4_1.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMXRT106x/NXP_iMXRT106x_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMXRT106x/NXP_iMXRT106x.pex
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX7ULP/NXP_iMX7ULP_BB_M4_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX7ULP/NXP_iMX7ULP_BB_A7_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX7ULP/NXP_iMX7ULP_CortexA7.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMX7ULP/NXP_iMX7ULP_CortexM4.JLinkScript
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMXRT5xx/Readme_NXP.txt
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMXRT5xx/MIMXRT5XX_FLEXSPI.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/NXP/iMXRT5xx/MIMXRT5XX_FLEXSPI_S.FLM
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ATMEL/SAMA5D2/SAMA5D2XPLAINED_QSPI.elf
%attr(0664,root,users) /opt/SEGGER/JLink_V662d/Devices/ATMEL/SAMB11/Atmel_ATSAMB11.elf
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkSWOViewerCLExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/JLinkRegistrationExe
%attr(0755,root,users) /opt/SEGGER/JLink_V662d/libjlinkarm_x86.so
/opt/SEGGER/JLink_V662d/libjlinkarm_x86.so
/usr/bin/JLinkRTTLoggerExe
/usr/bin/JMem
/usr/bin/JLinkSWOViewer_CL
/usr/bin/JFlashLiteExe
/usr/bin/JLinkGDBServerExe
/usr/bin/JLinkSWOViewerExe
/usr/bin/JRun
/usr/bin/JLinkRTTLogger
/usr/bin/JLinkGDBServer
/usr/bin/JLinkExe
/usr/bin/JLinkSTM32
/usr/bin/JLinkConfig
/usr/bin/JFlashSPICLExe
/usr/bin/JLinkRTTClient
/usr/bin/JMemExe
/usr/bin/JLinkRTTClientExe
/usr/bin/JLinkConfigExe
/usr/bin/JLinkRemoteServer
/usr/bin/JTAGLoadExe
/usr/bin/JLinkLicenseManagerExe
/usr/bin/JLinkSTM32Exe
/usr/bin/JLinkGUIServerExe
/usr/bin/JLinkRegistration
/usr/bin/JLinkGUIServer
/usr/bin/JFlashLite
/usr/bin/JLinkRemoteServerCLExe
/usr/bin/JRunExe
/usr/bin/JLinkGDBServerCLExe
/usr/bin/JLinkRTTViewerExe
/usr/bin/JLinkLicenseManager
/usr/bin/JFlashSPI_CL
/usr/bin/JLinkRemoteServerExe
/usr/bin/JLinkRTTViewer
/usr/bin/JLinkSWOViewer
/usr/bin/JLinkSWOViewerCLExe
/usr/bin/JLinkRegistrationExe

%pre
SYS_SYMLINK_DIR=/opt/SEGGER
echo "Removing ${SYS_SYMLINK_DIR}/JLink ..."
if [ -e ${SYS_SYMLINK_DIR}/JLink ]       # Does it exist?
then
  if  [ -h ${SYS_SYMLINK_DIR}/JLink ]    # Is it a symbolic link?
  then
    rm -f ${SYS_SYMLINK_DIR}/JLink
  elif  [ -d ${SYS_SYMLINK_DIR}/JLink ]  # Is it a real folder?
  then
    rm -f -r ${SYS_SYMLINK_DIR}/JLink
  else 
    echo "Error: please remove ${SYS_SYMLINK_DIR}/JLink"
    exit 1                               # Unexpected result
  fi
else
  echo "${SYS_SYMLINK_DIR}/JLink not found (OK)"
fi
exit 0