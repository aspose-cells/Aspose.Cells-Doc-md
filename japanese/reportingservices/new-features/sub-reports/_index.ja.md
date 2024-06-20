---
title: サブレポート
type: docs
weight: 20
url: /ja/reportingservices/sub-reports/
---

{{% alert color="primary" %}} 

テーブルグループ行にサブレポートを埋め込むサポートを組み込みました。フォーマットは次のとおりです:

&=subreport{ReportName=your report name; parameter1 name = parameter1 value; parameter2 name = parameter2 value;......} 

{{% /alert %}} 
### **例**
**テーブル内のサブレポート** 

![todo:image_alt_text](sub-reports_1.png)

例では、サブレポートの名前は「売上詳細」です。1つのパラメータ、*SalesOrderNumber* を持っています。パラメータの値は *EmpSalesDetail.SalesOrderNumber* です。
#### **サブレポートを使用する制限事項**
- サブレポートはAspose.Cells.Reporting Services Designerツールで設計する必要があります。
- サブレポートはテーブルグループ行にのみ埋め込むことができ、グループ行にはサブレポート以外の要素を含めることはできません。テーブルの詳細行やフッター行にサブレポートを埋め込むことはできません。
- 現在、1つ以上のレベルのネストはサポートされていません。サブレポートには埋め込みレポートを含めることはできません。
