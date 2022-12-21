---
title: アクセス ワークシート Cells
type: docs
weight: 10
url: /ja/net/access-worksheet-cells/
---
{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridWeb の最も基本的な機能であるセルへのアクセスを見て、セルについて説明します。

{{% /alert %}} 
## **ワークシートで Cells にアクセスする**
各ワークシートには、実際には GridCell オブジェクトのコレクションである Cells という名前のプロパティが含まれており、GridCell オブジェクトは Aspose.Cells.GridWeb のセルを表します。 Aspose.Cells.GridWeb を使用して任意のセルにアクセスできます。 2 つの好ましい方法があり、それぞれについて以下で説明します。


### **Cell名を使用**
すべてのセルには固有の名前があります。たとえば、A1、A2、B1、B2 などです。Aspose.Cells.GridWeb を使用すると、開発者はセル名を使用して目的のセルにアクセスできます。セル名を (インデックスとして) GridWorksheet の Cells コレクションに渡すだけです。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


### **行と列のインデックスの使用**
セルは、行インデックスと列インデックスの位置によっても認識できます。セルの行と列のインデックスを GridWorksheet の Cells コレクションに渡すだけです。このアプローチは、上記のアプローチよりも高速です。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}
