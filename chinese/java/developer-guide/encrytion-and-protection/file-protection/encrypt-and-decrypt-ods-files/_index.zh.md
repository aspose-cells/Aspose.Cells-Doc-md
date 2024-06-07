---
title: 加密和解密ODS文件
type: docs
weight: 10
url: /zh/java/encrypt-and-decrypt-ods-files/
description: 使用纯 Java 库 Aspose.Cells for Java 加密和密码保护 ODS 文件。
---

{{% alert color="primary" %}}
OpenOffice.org 是一款功能齐全的办公套件，支持对文件进行密码保护和加密。但是，加密的ODS文件只能在提供密码后由OpenOffice打开。Excel无法打开加密的ODS文件，可能会出现警告消息。与其他文件类型不同，加密选项不适用于ODS文件。 
Aspose.Cells 允许加密和解密ODS文件。解密后的ODS文件可以在Excel和OpenOffice中打开。 
{{% /alert %}}

## **使用OpenOffice Calc进行加密**
1. 选择 **另存为** 并点击 **另存时使用密码** 框。
1. 点击**保存**按钮。
1. 在打开的“设置密码”窗口的“输入密码以打开”和“确认密码”字段中输入所需的密码。 
1. 单击**确定**按钮以保存文件。

## **加密/解密 ODS 文件：**

要加密 ODS 文件，加载文件并在保存之前将实际密码传递给 [**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password)。生成的加密的 ODS 文件只能在 OpenOffice 中打开。要解密 ODS 文件，通过提供密码加载文件至 [**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password)，加载文件后，使用实际密码作为参数调用函数 [**Workbook.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String)，最后将 null 传递给 [**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password)。

### **示例代码:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
