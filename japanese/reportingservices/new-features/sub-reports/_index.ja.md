---
title: サブレポート
type: docs
weight: 20
url: /ja/reportingservices/sub-reports/
---
{{% alert color="primary" %}} 

テーブル グループ行にサブレポートを埋め込むためのサポートが組み込まれました。形式は次のとおりです。

&=subreport{ReportName=レポート名;パラメータ 1 の名前 = パラメータ 1 の値。パラメータ 2 の名前 = パラメータ 2 の値;......} 

{{% /alert %}} 
### **例**
**テーブル内のサブレポート** 

![todo:画像_代替_文章](sub-reports_1.png)

例では、サブレポートの名前は「Sales Order Detail」です。パラメータは1つ、*受注番号*.パラメータの値は*EmpSalesDetail.SalesOrderNumber.*
#### **サブレポートの使用に関する制限**
- サブレポートは、Aspose.Cells.Reporting Services Designer ツールを使用して設計する必要があります。
- サブレポートはテーブル グループ行にのみ埋め込むことができ、グループ行にはサブレポート以外の要素を含めることはできません。表の詳細行またはフッター行にサブレポートを埋め込むことはできません。
- 現在、複数レベルのネストはサポートされていません。サブレポートに埋め込みレポートを含めることはできません。
