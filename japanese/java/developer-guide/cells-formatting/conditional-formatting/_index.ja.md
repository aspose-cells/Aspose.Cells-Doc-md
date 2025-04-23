---
title: 条件付き書式設定
type: docs
weight: 120
url: /ja/java/conditional-formatting/
---

{{% alert color="primary" %}} 

条件付き書式設定は、Microsoft Excel の高度な機能であり、セルやセル範囲に書式を適用し、その書式をセルの値や式の値に応じて変更することができます。 例えば、セルの値が500を超える場合のみ太字で表示するようにすることができます。 セルの値が条件を満たした場合、指定された書式がセルに適用されます。 もしセルの値が条件を満たさない場合は、デフォルトの書式が使用されます。 Microsoft Excel では、**書式**、次いで **条件付き書式設定** を選択して、条件付き書式設定ダイアログを開くことができます。

**Microsoft Excel における条件付き書式設定** 

![todo:image_alt_text](conditional-formatting_1.png)

Aspose.Cells は、ランタイムでセルに条件付き書式設定を適用する機能をサポートしています。 この記事ではその方法について説明します。

{{% /alert %}} 
## **条件付き書式の適用**
Aspose.Cells は次の2つの方法で条件付き書式設定をサポートしています:

- [デザイナー スプレッドシートを使用](/cells/ja/java/conditional-formatting/)
- [ランタイムで条件付き書式設定を作成](/cells/ja/java/conditional-formatting/)
### **デザイナー スプレッドシートを使用**
開発者は、Microsoft Excel で条件付き書式設定を含むデザイナー スプレッドシートを作成し、それを Aspose.Cells で開くことができます。 Aspose.Cells はデザイナー スプレッドシートを読み込み、保存し、条件付き書式設定を保持します。 デザイナー スプレッドシートについて詳しく知りたい場合は、[デザイナー スプレッドシートとは](/cells/ja/java/what-is-a-designer-spreadsheet/) を参照してください。
## **ランタイムで条件付き書式を適用**
Aspose.Cells は、ランタイムで条件付き書式設定を適用する機能をサポートしています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConditionalFormattingatRuntime-ConditionalFormattingatRuntime.java" >}}
### **フォントの設定**
**Microsoft Excel でのフォントの設定** 

![todo:image_alt_text](conditional-formatting_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontStyle-SettingFontStyle.java" >}}
### **境界線の設定**
**Microsoft Excel での罫線の設定** 

![todo:image_alt_text](conditional-formatting_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetBorder-SetBorder.java" >}}
### **パターンの設定**
**Microsoft Excel でのセルのパターンの設定** 

![todo:image_alt_text](conditional-formatting_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetPattern-SetPattern.java" >}}

## **高度なトピック**
- [セルのテキストと条件付きアイコンセットの追加](/cells/ja/java/add-conditional-icons-set-with-the-cell-text/)
- [2色系規則と3色系規則の条件付き書式設定を追加する](/cells/ja/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [ワークシートで条件付き書式設定を適用する](/cells/ja/java/apply-conditional-formatting-in-worksheets/)
- [条件付き書式設定を使用して、交互に行と列に影を付ける](/cells/ja/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)

{{< app/cells/assistant language="java" >}}
