---
title: グリッド線と行の列ヘッダーの表示と非表示
type: docs
weight: 30
url: /ja/net/show-and-hide-gridlines-and-row-column-headers/
---
{{% alert color="primary" %}}

Aspose.Cells は、デフォルトで表示されるワークシートのグリッド線の表示と非表示をサポートします。また、ワークシートの行列ヘッダーの可視性を制御することもできます。

{{% /alert %}}

## **グリッド線の表示と非表示**

すべての Excel ワークシートには、既定でグリッド線があります。特定のセルにデータを簡単に入力できるように、セルの輪郭を描くのに役立ちます。グリッド線を使用すると、ワークシートをセルのコレクションとして表示でき、各セルを簡単に識別できます。

### **グリッド線の可視性の制御**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)開発者が Excel ファイル内の各ワークシートにアクセスできるようにするコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。グリッド線の可視性を制御するには、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)財産。[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)ブール型のプロパティです。つまり、格納できるのは**真実**また**間違い**価値。

#### **グリッド線を表示する**

を設定して、グリッド線を表示します。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)プロパティへ**真実**.

#### **グリッド線を非表示にする**

を設定してグリッド線を非表示にします。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)プロパティへ**間違い**.

の使用を示す完全な例を以下に示します。[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)Excel ファイル (book1.xls) を開き、最初のワークシートのグリッド線を非表示にして、変更したファイルを output.xls として保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **行の列ヘッダーの表示と非表示**

Excel ファイル内のすべてのワークシートは、行と列に配置されたセルで構成されています。すべての行と列には、それらを識別し、個々のセルを識別するために使用される一意の値があります。たとえば、行には 1、2、3、4 などの番号が付けられ、列は A、B、C、D などのアルファベット順に並べられます。行と列の値はヘッダーに表示されます。開発者は、Aspose.Cells を使用して、これらの行と列のヘッダーの表示を制御できます。

### **ワークシートの表示の制御**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)開発者が Excel ファイル内の各ワークシートにアクセスできるようにするコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティとメソッドが用意されています。行ヘッダーと列ヘッダーの表示を制御するには、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)財産。[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)ブール型のプロパティです。つまり、格納できるのは**真実**また**間違い**価値。

#### **行/列ヘッダーを表示する**

を設定して、行と列のヘッダーを表示します。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)プロパティへ**真実**.

#### **行/列ヘッダーの非表示**

を設定して、行と列のヘッダーを非表示にします。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)プロパティへ**間違い**.

の使用方法を示す完全な例を以下に示します。[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)Excel ファイル (book1.xls) を開き、最初のワークシートの行ヘッダーと列ヘッダーを非表示にして、変更したファイルを output.xls として保存します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

を使用することも可能です[**再表示行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows)と[**非表示の列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)のメソッド[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)複数の行と列を表示するためのクラス。

{{% /alert %}}
