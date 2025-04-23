---
title: Aspose.Cells 8.6.0 での Public API 変更
type: docs
weight: 200
url: /ja/java/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cells API のバージョン 8.5.2 から 8.6.0 への変更点について説明しており、モジュール/アプリケーション開発者に興味を持たれるかもしれません。[追加されたクラスなど](/cells/ja/java/public-api-changes-in-aspose-cells-8-6-0/)だけでなく、Aspose.Cells の内部動作の変更についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **Workbook のオブジェクトを生成せずにメタデータ操作をサポート**
このリリースの Aspose.Cells for Java API では、WorkbookMetadata & MetadataOptions という新しいクラスが公開され、また新しい列挙型 MetadataType が追加され、これにより、Workbook インスタンスを作成せずにドキュメントプロパティ（メタデータ）を操作することが可能となりました。WorkbookMetadata クラスは軽量で使いやすく、パフォーマンスに影響を与えることなく、文書のプロパティを読み書き更新するメカニズムを提供します。 

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Open Workbook metadata while specifying the appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DOCUMENT_PROPERTIES);

WorkbookMetadata metaWorkbook = new WorkbookMetadata("sample.xlsx", options);

//Set some properties

metaWorkbook.getCustomDocumentProperties().add("test", "test");

//Save the metadata information to the spreadsheet file

metaWorkbook.save(filePath);

{{< /highlight >}}
### **HtmlSaveOptions.ExportFrameScriptsAndProperties プロパティが追加されました**
Aspose.Cells for Java 8.6.0 では、HtmlSaveOptions.ExportFrameScriptsAndProperties プロパティが公開され、スプレッドシートを HTML 形式に変換する際に追加のスクリプトを作成する影響を与えることができます。デフォルト設定では、Aspose.Cells API は、結果として生成される HTML がフレームや条件付きコメントを含むため、ブラウザの種類を検出し、レイアウトを調整します。HtmlSaveOptions.ExportFrameScriptsAndProperties プロパティのデフォルト値は true であり、つまり、エクスポートは Excel の基準に従って行われます。プロパティを false に設定すると、API は[フレームと条件付きコメントに関連するスクリプトを生成しません](/cells/ja/java/disable-exporting-frame-scripts-and-document-properties/)。この場合、生成された HTML は任意のブラウザで正しく表示できますが、Aspose.Cells API を使用して戻すことはできません。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.setExportFrameScriptsAndProperties(false);

//Save spreadsheet as HTML

book.save("output.html", options)

{{< /highlight >}}
### **Shape.MarcoName プロパティが追加されました**
Aspose.Cells for Java 8.6.0 では、Shape.MarcoName プロパティが公開され、Button などのフォームコントロールに VBA モジュールを[割り当てること](/cells/ja/java/assign-macro-code-to-form-control/)ができます。プロパティは string 型であり、したがって、モジュール名を受け入れ、コントロールに割り当てます。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create a new Workbook object

Workbook workbook = new Workbook();

//Get the instance of first default worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Add a new module to the first worksheet

int moduleIdx = workbook.getVbaProject().getModules().add(sheet);

//Get the instance of newly added module

VbaModule module = workbook.getVbaProject().getModules().get(moduleIdx);

//Add module code

module.setCodes("Sub ShowMessage()" + "\r\n" +

        "    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

        "End Sub");

//Create a new button to the worksheet and set its various properties

Button button = (Button) sheet.getShapes().addShape(MsoDrawingType.BUTTON, 2, 0, 2, 0, 28, 80);

button.setPlacement(PlacementType.FREE_FLOATING);

button.getFont().setName("Tahoma");

button.getFont().setBold(true);

button.getFont().setColor(Color.getBlue());

button.setText("Aspose");

//Assign the newly added module to the button

button.setMacroName(module.getName() + ".ShowMessage" );

//Save the spreadsheet in XLSM format

workbook.save("output.xlsm");

{{< /highlight >}}
### **OoxmlSaveOptions.UpdateZoom プロパティが追加されました**
v8.6.0 でのリリースにより、Aspose.Cells for Java API は、OoxmlSaveOptions.UpdateZoom プロパティを公開し、Worksheet のスケーリングを制御するために PageSetup.FitToPagesWide および/または PageSetup.FitToPagesTall プロパティが使用された場合に、PageSetup.Zoom を更新するために使用できます。
{{< app/cells/assistant language="java" >}}
