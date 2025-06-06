---
title: 宣言
type: docs
weight: 30
url: /ja/net/declaration/
---

{{% alert color="primary" %}} 

一般的に、すべてのAspose .NETコンポーネントにはフルトラスト権限が必要です。その理由は、Aspose for .NETコンポーネントがフォントの解析などの特定の操作のために、登録表の設定、仮想ディレクトリ以外のシステムファイルへのアクセスが必要だからです。また、Aspose for .NETコンポーネント（Aspose.Cells for .NETを含む）は、多くの場合フルトラスト権限が必要なコア.NETシステムクラスに基づいています。

{{% /alert %}} 
## **部分信頼/中間信頼の課題**
異なる企業からの複数のアプリケーションをホストしているインターネットサービスプロバイダは、主に中間信頼セキュリティレベルを強制します。また、ISPなどの共有サーバーに複数のアプリケーションをホストする必要がある場合、ASP.NET中間信頼レベルを使用してアプリケーションを制約する必要があります。.NET 2.0の場合、そのようなセキュリティレベルは、または次の制約を設定する場合があります。これは、たとえば、Aspose.Cells for .NETが正常に機能する能力に影響を与える可能性がある制約を提供します:

- **RegistryPermissionが利用できません**。これは、スプレッドシートや他の文書をレンダリングする際に、インストールされたフォントを列挙するために必要な登録表にアクセスできないことを意味します。
- **FileIOPermission is restricted**. これは、アプリケーションの仮想ディレクトリ階層内のファイルにのみアクセスできることを意味します。これは、エクスポート中にフォントを読み取ることができない可能性があります。
## **Medium Trust Permissions SetでAspose.Cells for .NETを使用します**
Medium Trustレベルまたは共有サーバー環境でAspose.Cells for .NETを実行するためのいくつかの推奨事項に従うことができます:

- コード内でライセンスファイルを設定するために、ライセンスファイルをストリームに取得した後にLicense.SetLicense(Stream)メソッドを呼び出すことが良いでしょう。
- フォントディレクトリ（許可付きでアクセス可能な場合）を設定する必要があります。サーバー上でファイルにアクセスする方法がない場合は、必要なフォントファイルをアプリケーションに追加してください。
- 部分信頼モードでは、Shape-to-EMF変換はサポートされていないため、（シェイプ用の）エクスポートされたイメージタイプを別の画像形式に設定してください。

Medium TrustモードでAspose.Cells for .NETを使用/実行する例は以下を参照してください:

{{< highlight csharp >}}

 // Instantiate the License object

Aspose.Cells.License lic = new Aspose.Cells.License();

// Get the license file into stream

System.IO.Stream stream = System.IO.File.OpenRead(MapPath("~") + @"\Aspose.Cells.lic");

// Set the License stream

lic.SetLicense(stream);

// Close the stream

stream.Close();

// Set the fonts directory

CellsHelper.FontDir = MapPath("~") + @"\Fonts";

//Open the template file

Workbook workbook = new Workbook(MapPath("~") + @"\test.xlsx");

PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();

// Set the image type to other format instead of using the default image type, that is, EMF

pdfSaveOptions.ImageType = System.Drawing.Imaging.ImageFormat.Png;

// Save the PDF file

workbook.Save(MapPath("~") + @"\dest.pdf", pdfSaveOptions);

// Save the XLSX file

workbook.Save(MapPath("~") + @"\dest.xlsx");



{{< /highlight >}}





{{< app/cells/assistant language="csharp" >}}
