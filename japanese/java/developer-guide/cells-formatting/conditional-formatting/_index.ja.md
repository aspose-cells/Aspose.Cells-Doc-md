---
title: 条件付き書式
type: docs
weight: 120
url: /ja/java/conditional-formatting/
---
{{% alert color="primary" %}} 

条件付き書式は、セルまたはセル範囲に書式を適用し、セルの値または数式の値に応じて書式を変更できる高度な Microsoft Excel 機能です。たとえば、セルの値が 500 より大きい場合にのみ、セルを太字で表示することができます。セルの値が条件を満たすと、指定された書式がセルに適用されます。セルの値が条件を満たさない場合は、既定の書式設定が使用されます。 Microsoft Excel で、**フォーマット**、 それから**条件付き書式**をクリックして、条件付き書式設定ダイアログを開きます。

**Microsoft Excel の条件付き書式** 

![todo:画像_代替_文章](conditional-formatting_1.png)

Aspose.Cells は、実行時に条件付き書式をセルに適用することをサポートします。この記事では、その方法について説明します。

{{% /alert %}} 
## **条件付き書式の適用**
Aspose.Cells は、次の 2 つの方法で条件付き書式をサポートします。

- [デザイナー スプレッドシートの使用](/cells/ja/java/conditional-formatting/).
- [実行時に条件付き書式を作成する](/cells/ja/java/conditional-formatting/).
### **Designer スプレッドシートの使用**
開発者は、Microsoft Excel で条件付き書式を含むデザイナー スプレッドシートを作成し、そのスプレッドシートを Aspose.Cells で開くことができます。デザイナー スプレッドシートの詳細については、以下をお読みください。[Designer スプレッドシートとは](/cells/ja/java/what-is-a-designer-spreadsheet/).
## **実行時に条件付き書式を適用する**
Aspose.Cells は、実行時の条件付き書式の適用をサポートします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConditionalFormattingatRuntime-ConditionalFormattingatRuntime.java" >}}
### **フォントの設定**
**Microsoft エクセルのフォント設定** 

![todo:画像_代替_文章](conditional-formatting_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontStyle-SettingFontStyle.java" >}}
### **境界線を設定**
**Microsoft Excelで罫線を設定する** 

![todo:画像_代替_文章](conditional-formatting_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetBorder-SetBorder.java" >}}
### **パターンの設定**
**Microsoft Excelでセルパターンを設定する** 

![todo:画像_代替_文章](conditional-formatting_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetPattern-SetPattern.java" >}}

## **先行トピック**
- [Cell テキストで設定された条件付きアイコンを追加する](/cells/ja/java/add-conditional-icons-set-with-the-cell-text/)
- [色スケールおよび 3 色スケールの条件付き書式の追加](/cells/ja/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [ワークシートに条件付き書式を適用する](/cells/ja/java/apply-conditional-formatting-in-worksheets/)
- [条件付き書式を使用して交互の行と列に陰影を適用する](/cells/ja/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)

