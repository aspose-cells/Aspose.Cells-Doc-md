---
title: グリッド線と行列ヘッダーの表示および非表示
type: docs
weight: 30
url: /ja/net/show-and-hide-gridlines-and-row-column-headers/
description: この記事では、C# APIまたは.NETライブラリを使用してExcelワークシートのグリッド線、行、列のヘッダーをプログラムで非表示または表示するサンプルコードを提供しています。
---

{{% alert color="primary" %}}

Aspose.Cellsは、デフォルトで表示されているワークシートのグリッド線の非表示および表示をサポートしています。また、ワークシートの行列ヘッダーの表示を制御する機能も提供しています。

{{% /alert %}}

## **グリッド線の表示と非表示**

すべてのExcelワークシートはデフォルトでグリッド線を持っています。これにより、特定のセルにデータを入力することが簡単になります。グリッド線により、ワークシートをセルのコレクションとして表示し、各セルを簡単に識別することができます。

### **グリッド線の表示の制御**

Aspose.Cellsでは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスが提供されています。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスにはExcelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するためのさまざまなプロパティやメソッドが提供されています。グリッド線の表示を制御するには、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスの[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)プロパティを使用します。[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)は真偽値プロパティであり、**true**または**false**の値のみを格納できます。

#### **グリッド線を表示する**

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスの[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)プロパティを**true**に設定することでグリッド線を表示します。

#### **グリッド線を非表示にする**

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスの[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)プロパティを**false**に設定することでグリッド線を非表示にします。

以下に完全な例が示されており、[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)のプロパティを使用して、Excelファイル（book1.xls）を開き、最初のワークシートでグリッド線を非表示にし、変更されたファイルをoutput.xlsとして保存する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **行列ヘッダーの表示および非表示**

Excelファイルのすべてのワークシートは、行と列で配置されたセルから構成されています。すべての行と列には、それぞれユニークな値があり、行と列、また個々のセルを識別するために使用されます。たとえば、行には数字が付いています- 1、2、3、4など- そして列はアルファベット順に並んでいます- A、B、C、Dなど- 行と列の値はヘッダーに表示されます。Aspose.Cellsを使用すると、これらの行列ヘッダーの表示を制御することができます。

### **ワークシートの表示を制御する**

Aspose.Cellsでは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスが提供されています。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスにはExcelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは、ワークシートを管理するための幅広いプロパティやメソッドが提供されています。行と列のヘッダーの表示を制御するには、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスの[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)プロパティを使用します。[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)は真偽値プロパティであり、**true**または**false**の値のみを格納できます。

#### **行/列ヘッダーを表示する**

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスの[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)プロパティを**true**に設定することで行と列のヘッダーを表示します。

#### **行/列ヘッダーを非表示にする**

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスの[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)プロパティを**false**に設定することで行と列のヘッダーを非表示にします。

以下に完全な例が示されており、[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)のプロパティを使用して、Excelファイル（book1.xls）を開き、最初のワークシートで行と列のヘッダーを非表示にし、変更されたファイルをoutput.xlsとして保存する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

また、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラスの[**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows)メソッドと[**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)メソッドを使用して、複数の行と列を表示したり非表示にしたりすることも可能です。

{{% /alert %}}
