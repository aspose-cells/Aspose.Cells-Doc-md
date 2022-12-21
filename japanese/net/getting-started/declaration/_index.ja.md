---
title: 宣言
type: docs
weight: 30
url: /ja/net/declaration/
---
{{% alert color="primary" %}} 

通常、すべての Aspose .NET コンポーネントには、完全な信頼のアクセス許可が設定されている必要があります。その理由は、Aspose for .NET コンポーネントがレジストリ設定、フォントの解析などの特定の操作のための仮想ディレクトリ以外のシステム ファイルにアクセスする必要があるためです。多くの場合設定されます。

{{% /alert %}} 
## **部分的な信頼 / 中程度の信頼のチャレンジ**
さまざまな企業の複数のアプリケーションをホストするインターネット サービス プロバイダーは、ほとんどの場合、中程度の信頼のセキュリティ レベルを適用します。さらに、ISP やその他のシナリオなど、共有サーバーで複数のアプリケーションをホストする必要がある場合は、中程度の信頼レベルを使用してアプリケーションを制限する必要があります。 ASP.NET 中信頼レベルは、ISP サーバーでホストされている複数のアプリケーションを分離するのに適した、制約付きの実行環境を提供します。 .NET 2.0 の場合、このようなセキュリティ レベルは、Aspose.Cells for .NET の適切な実行能力に影響を与える可能性のある次の制約を設定する可能性があります。たとえば:

- **RegistryPermission は利用できません**.これは、スプレッドシートやその他のドキュメントをレンダリングするときに、インストールされているフォントを列挙するために必要なレジストリにアクセスできないことを意味します。
- **FileIOPermission は制限されています**.これは、アプリケーションの仮想ディレクトリ階層内のファイルにのみアクセスできることを意味します。これは、エクスポート中にフォントを読み取れないことを意味する可能性があります。
## **中程度の信頼のアクセス許可セットで Aspose.Cells for .NET を使用する**
中程度の信頼レベルまたは共有サーバー環境で Aspose.Cells for .NET を実行するためのいくつかの推奨事項に従うことができます。

- コードでライセンス ファイルを設定するには、ライセンス ファイルをストリームに取得した後で、代わりに License.SetLicense(Stream) メソッドを呼び出すことをお勧めします。
- フォントのディレクトリ (許可を得てアクセスできる) を設定する必要があります。サーバー上のファイルにアクセスする方法がない場合は、必要なフォント ファイルをアプリケーションに追加してください。
- 部分信頼モードでは、形状から EMF への変換はサポートされていないため、エクスポートされた画像の種類 (形状の場合) を別の画像形式に設定します。

ミディアム トラスト モードで Aspose.Cells for .NET を使用/実行する方法を示す次の例を参照してください。

{{< highlight "csharp" >}}

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





