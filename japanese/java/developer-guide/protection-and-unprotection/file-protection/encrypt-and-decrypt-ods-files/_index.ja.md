---
title: ODSファイルの暗号化と複合化
type: docs
weight: 10
url: /ja/java/encrypt-and-decrypt-ods-files/
description: 純粋なJavaライブラリであるAspose.Cells for Javaを使用して、ODSファイルにパスワードを設定し、暗号化することができます。
---

{{% alert color="primary" %}}
OpenOffice.orgはパスワード保護とファイルの暗号化をサポートする完全な機能を備えたオフィススイートです。ただし、暗号化されたODSファイルはパスワードを提供した後にのみOpenOfficeで開くことができ、Excelは暗号化されたODSファイルを開くことはできません。暗号化オプションは、その他のファイルタイプとは異なり、ODSファイルには適用されません。 
Aspose.Cellsを使用して、ODSファイルの暗号化と複合化が可能です。複合されたODSファイルはExcelとOpenOfficeの両方で開くことができます。 
{{% /alert %}}

## **OpenOffice Calcで暗号化**
1. 「名前を付けて保存」を選択し、「パスワードで保存」ボックスをクリックします。
1. **保存**ボタンをクリックします。
1. 開いた「パスワードの設定」ウィンドウの「開くためのパスワードを入力」および「パスワードを確認」フィールドに希望するパスワードを入力します。 
1. ファイルを保存するために **OK** ボタンをクリックします。

## **ODSファイルの暗号化/復号化:**

ODSファイルを暗号化するには、ファイルを読み込み、保存する前に実際のパスワードを [**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password) に渡します。出力される暗号化されたODSファイルはOpenOfficeでのみ開くことができます。ODSファイルを復号化するには、[**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password) にパスワードを提供してファイルを読み込みます。ファイルを読み込んだ後は、実際のパスワードを引数として関数 [**Workbook.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect-java.lang.String-) を呼び出し、最後に [**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password) にnullを渡します。

### **サンプルコード:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
{{< app/cells/assistant language="java" >}}
