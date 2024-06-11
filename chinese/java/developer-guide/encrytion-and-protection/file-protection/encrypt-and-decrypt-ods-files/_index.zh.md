---
title: 加密和解密ODS文件
type: docs
weight: 10
url: /zh/java/encrypt-and-decrypt-ods-files/
description: 使用Aspose.Cells for Java密码保护和加密ODS文件，这是一个纯Java库。
---

{{% alert color="primary" %}}
OpenOffice.org是一个功能齐全的办公套件，支持对文件进行密码保护和加密。然而，加密的ODS文件只能在提供密码后才能在OpenOffice中打开。Excel无法打开加密的ODS文件，可能会弹出警告消息。与其他文件类型不同，加密选项不适用于ODS文件。 
Aspose.Cells允许对ODS文件进行加密和解密。解密的ODS文件可以同时在Excel和OpenOffice中打开。 
{{% /alert %}}

## **在OpenOffice Calc中加密**
1. 选择**另存为**并点击**加上密码保存**框。
1. 点击**保存**按钮。
1. 在打开密码窗口中的**输入打开文件的密码**和**确认密码**字段中键入所需的密码。 
1. 点击**确定**按钮以保存文件。

## **加密/解密ODS文件**

对ODS文件进行加密时，加载文件并在保存之前传递实际密码给[**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password)。输出的加密ODS文件只能在OpenOffice中打开。对ODS文件进行解密时，通过在[**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password)中提供密码来加载文件。加载文件后，使用实际密码调用函数[**Workbook.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String)，最后给[**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password)传递null。

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
