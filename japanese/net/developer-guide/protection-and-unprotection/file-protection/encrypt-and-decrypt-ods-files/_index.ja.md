---
title: ODSファイルの暗号化と複合化
type: docs
weight: 10
url: /ja/net/encrypt-and-decrypt-ods-files/
description: Aspose.Cells for .NETを使用してODSファイルをパスワード保護および暗号化する
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

## **Aspose.Cells for .NETでODSファイルを暗号化**
ODSファイルを暗号化するには、ファイルを読み込んで保存する前に[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)の値を実際のパスワードに設定します。出力される暗号化されたODSファイルは、OpenOfficeでのみ開くことができます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **Aspose.Cells for .NETでODSファイルを複合化**

ODSファイルを復号化するには、[**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password)によるパスワードの提供でファイルを読み込みます。ファイルが読み込まれたら、[**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password)文字列をnullに設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
