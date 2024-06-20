---
title: レポートパラメータをレポートに追加
type: docs
weight: 60
url: /ja/reportingservices/adding-report-parameters-to-report/
---

{{% alert color="primary" %}} 

Aspose.Cellsのレポートテンプレートは、Reporting Servicesレポートパラメータを含むセルのデータソースとしてReporting Servicesレポートパラメータマーカーを持つものをサポートします。Reporting Servicesパラメータマーカーについては、[Aspose.Cellsテンプレートとスマートマーカー](/cells/ja/reportingservices/aspose-cells-template-and-smart-markers/)を参照してください。レポートパラメータは通常、テーブルヘッダーやフッターのテキストエリアに配置されます。

{{% /alert %}} 
### **レポートパラメーターの追加**
レポートにレポートパラメーターを追加するには：

1. セルを選択します。 

   **セルの選択** 

![todo:image_alt_text](adding-report-parameters-to-report_1.png)




1. Aspose.Cells.Report.Designerのツールバーで[挿入]式をクリックします(

![todo:image_alt_text](adding-report-parameters-to-report_2.png)

).

1. パラメーターパネルから**パラメータ**を選択します。
   すべてのパラメータは右側のパネルにリストされています。 
1. パラメータを選択し、例ではEmpIDを選択しました。
1. パラメータをダブルクリックして、フォームの上部に式を表示します。
   パラメータにはラベルと値（デフォルト属性は値）の2つのデータ属性があります。 

   **パラメーターの選択** 

![todo:image_alt_text](adding-report-parameters-to-report_3.png)




1. サンプルでは、パラメータのラベルがレポートに表示されるように、式をParameters!EmpID.Labelに変更します。 

   **パラメーターの変更** 

![todo:image_alt_text](adding-report-parameters-to-report_4.png)




1. **OK** をクリックします。
   選択したセルにはレポートパラメーターマーカーが含まれています。 

   **セルに挿入されたレポートパラメーター** 

![todo:image_alt_text](adding-report-parameters-to-report_5.png)
