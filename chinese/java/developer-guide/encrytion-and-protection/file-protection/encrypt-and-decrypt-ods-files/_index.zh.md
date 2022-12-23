---
title: 加密和解密 ODS 个文件
type: docs
weight: 10
url: /zh/java/encrypt-and-decrypt-ods-files/
description: 使用 Aspose.Cells for Java 密码保护和加密 ODS 文件，这是一个纯 Java 库。
---
{{% alert color="primary" %}}
OpenOffice.org 是一个功能齐全的办公套件，支持密码保护和加密文件。然而加密的ODS文件只有在提供密码后才能被OpenOffice打开。 Excel 无法打开加密的 ODS 文件，可能会引发警告消息。与其他文件类型不同，加密选项不适用于 ODS 文件。
 Aspose.Cells 允许加密和解密 ODS 文件。解密后的ODS文件可以在Excel和OpenOffice中打开，
{{% /alert %}}

## **使用 OpenOffice Calc 加密**
1. 选择**另存为**并点击**用密码保存**盒子。
1. 点击**救球**按钮。
1. 在两者中输入您想要的密码**输入密码打开**和**确认密码**打开的“设置密码”窗口中的字段。
1. 点击**好的**按钮保存文件。

## **加密/解密 ODS 文件：**

为了加密 ODS 文件，加载文件并将实际密码传递给[**工作簿设置.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password)在保存之前。输出的加密文件ODS只能在OpenOffice中打开。要解密 ODS 文件，请通过在[**LoadOptions.setPassword() 方法**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password).加载文件后，调用函数[**工作簿.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String) ) 以实际密码作为参数，最后将 null 传递给[**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **示例代码：**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
