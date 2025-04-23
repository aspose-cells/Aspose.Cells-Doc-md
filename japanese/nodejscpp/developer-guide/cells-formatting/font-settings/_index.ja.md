---  
title: フォント設定をNode.js経由のC++で  
linktitle: フォント設定  
description: Aspose.Cellsは、スプレッドシートファイルを操作するためのNode.jsライブラリです。セルのフォントスタイルやプロパティをカスタマイズ可能に設定できます。この記事では、Aspose.Cellsライブラリを使用してセルのフォント設定を行う方法を紹介します。  
keywords: Aspose.Cells、セル、フォント設定、スタイル、プロパティ、Node.jsをC++経由で  
type: docs  
weight: 30  
url: /ja/nodejs-cpp/cells-font-settings/  
---  

{{% alert color="primary" %}}  
テキストの見た目はフォント設定を変更することでコントロールできます。フォント設定にはフォントの名前、スタイル、サイズ、色、その他の効果が含まれる場合があります。Microsoft Excelと同様に、Aspose.Cellsもセルのフォント設定をサポートしています。  
{{% /alert %}}  

## **フォント設定の構成**  

Aspose.Cellsは、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を提供しています。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスは、Excelファイル内の各ワークシートへアクセスできる[**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションを提供し、その中の各アイテムは[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスのオブジェクトを表します。  

Aspose.Cellsは、セルの書式設定スタイルを取得および設定に使用される[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)クラスの[**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--)および[**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)メソッドを提供します。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)クラスはフォント設定を構成するためのプロパティを提供します。  

### **フォント名の設定**  

開発者は、[**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)オブジェクトの[setName](https://reference.aspose.com/cells/nodejs-cpp/font/#setName-string-)メソッドを使用して、セル内のテキストに任意のフォントを適用できます。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontName.js" >}}


### **太字にフォントスタイルを設定する**  

開発者は、[**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)オブジェクトの[**setIsBold**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsBold-boolean-)メソッドを**true**に設定して、テキストを太字にできます。   

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetBoldStyle.js" >}}



### **フォントサイズの設定**  

[**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)オブジェクトの[**setSize**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSize-number-)メソッドを使用してフォントサイズを設定します。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontSize.js" >}}


### **フォントの色の設定**  

[**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)オブジェクトの[**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-)メソッドを使用してフォントの色を設定します。Color列挙体（Node.jsの一部）から任意の色を選択し、[**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-)メソッドに割り当てます。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontColor.js" >}}


### **フォントの下線タイプの設定**  

[**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)オブジェクトの[**setUnderline**](https://reference.aspose.com/cells/nodejs-cpp/font/#setUnderline-fontunderlinetype-)メソッドを使用してテキストに下線を引きます。Aspose.Cellsは、[**FontUnderlineType**](https://reference.aspose.com/cells/nodejs-cpp/fontunderlinetype)列挙体にさまざまな事前定義されたフォント下線タイプを提供します。  

|**フォントの下線の種類**|**説明**|  
| :- | :- |  
|Accounting|単一のアカウンティング下線  
|Double|ダブル下線  
|DoubleAccounting|ダブルアカウンティング下線  
|None|下線なし  
|Single|単一の下線  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontUnderline.js" >}}


### **取り消し線の効果の設定**  

[**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)オブジェクトの[**setIsStrikeout**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsStrikeout-boolean-)メソッドを**true**に設定して取消線を適用します。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}


### **下付き文字の効果の設定**  

[**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)オブジェクトの[**setIsSubscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSubscript-boolean-)メソッドを**true**に設定して下付き文字を適用します。  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}



### **フォントの上付き文字効果の設定**  

開発者は、[**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)オブジェクトの[**setIsSuperscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSuperscript-boolean-)メソッドを**true**に設定して上付き文字の効果を適用できます。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetSuperscript.js" >}}


## **高度なトピック**  
- [フォントに上付き文字および下付き文字効果を適用する](/cells/ja/nodejs-cpp/apply-superscript-and-subscript-effects-on-fonts/)  
- [スプレッドシートまたはブックで使用されているフォントのリストを取得する](/cells/ja/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)  


