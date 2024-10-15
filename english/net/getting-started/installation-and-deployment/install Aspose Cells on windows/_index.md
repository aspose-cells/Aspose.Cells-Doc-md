---
title: Install Aspose.Cells on Windows
type: docs
weight: 20
url: /net/installing-aspose-cells-on-windows/
---

{{% alert color="primary" %}} 

Sometimes you might face some problems installing **Aspose.Cells** using its installer package (Aspose.Cells.msi...Windows Installer Package) on **Windows Vista**. This document explains how we can cope with it and implement the successful installation of the component. Actually **Aspose.Cells** installer needs to create a virtual folder on IIS for the deployment of its Web Demos (Asp.NET Demos) on your machine, so you need to have an Administration Privileges before installing **Aspose.Cells** using its installer. The installer demands administrator-level access to the system must be explicitly allowed to do so.

{{% /alert %}} 
## **Possible Factors**
Normally, in **Windows Vista**, the products/components that you install/use are always implemented under "normal user" permissions, even if you are an **Administrator**. The programs are only allowed limited access to the file system, even if you are logged in as an **Administrator**. This has some unfortunate side effects that you normally wouldn't encounter in Windows XP when logged in as an **Administrator**.
## **UAC (User Account Control)**
**UAC** is the part of **Windows Vista** that asks you for permission. The **UAC** mode (also known as **Admin Approval Mode**) is a mode of operation that (primarily) affects the way administrator accounts work. When **UAC** is turned on (which it is by default), you must explicitly give permission to any program that wants to use "administrator" powers. Any program that tries to use admin powers without your permission will be denied access. **UAC** is also required for other security features of **Windows Vista**, including **Protected Mode** in Internet Explorer. Internet Explorer Protected Mode protects your computer from rogue web pages and other web-related vulnerabilities, including unknown ones.

When **UAC** mode is enabled, every program that you run will be given only "standard user" access to the system, even when you are logged in as an administrator. **Windows Vista** has the built-in ability to automatically reduce the potential of security breeches in the system. It does that by automatically enabling this feature called **User Account Control** (or **UAC** for short). The **UAC** forces users that are part of the local administrators group to run like they were regular users with no administrative privileges. Although **UAC** clearly improves the security on **Windows Vista**, under some scenarios you might want to disable it, for example when giving demos in front of an audience (demos that are not security related, for example). Some home users might be tempted to disable **UAC** because of the usage of additional resources of their system.
## **Steps Involved for Successful Installation of the Component**
- Please make sure that IIS is installed on your Vista before installing **Aspose.Cells**. It is compulsory because **Aspose.Cells** installer needs to create a virtual folder on IIS for the deployment of the Web Demos (Asp.NET Demos).
- You need to disable **UAC** (User Account Control). You have to make sure that you have an **Administrator Privileges** with full Control of the system before installing **Aspose.Cells**. Otherwise you might get an error # 2869 while installing **Aspose.Cells** using its installer.

Following are some ways to achieve this.
### **Using Command Line**
1. Search for cmd.exe into your windows directory, then right click on it and select Run as... **Administrator**
2. Now, Run the following command on command prompt: msiexec /i <your path>/Aspose.Cells.msi and Enter.
### **Using Control Panel**
- Click Start
- Click Control Panel
- Click User Accounts and Family Safety
- Click User Accounts
- Click Turn User Account Control On or Off
- Uncheck the checkbox
- Click OK

{{% alert color="primary" %}} 

You will need to restart your computer for the change to take effect. This change affects all accounts on the computer, not just yours.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}