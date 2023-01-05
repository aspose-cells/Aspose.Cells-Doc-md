---
title: サブレポート
type: docs
weight: 90
url: /ja/reportingservices/sub-report/
---
{{% alert color="primary" %}} 

サブレポートは、テーブル アイテムに埋め込むことができます。形式は次のとおりです。 &=subreport{ReportName=レポート名;パラメータ 1 の名前 = パラメータ 1 の値。パラメータ 2 の名前 = パラメータ 2 の値。 ...}

**レポート定義のサブレポート** 

![todo:画像_代替_文章](sub-report_1.png)

例では、サブレポートの名前は「Sales Order Detail」です。これには、SalesOrderNumber という 1 つのパラメーターがあります。パラメータの値は EmpSalesDetail.SalesOrderNumber です。
### **サブレポートの制限**
1. サブレポートは、Aspose.Cells.ReportingServices Designer で設計する必要があります。
1. サブレポートはテーブル グループ行にのみ埋め込むことができ、グループ行にはサブレポート以外の要素を含めることはできません。テーブルの詳細行またはフッター行にサブレポートを埋め込むことはできません。
1. 現在、複数レベルのネストはサポートされていません。サブレポートに埋め込みレポートを含めることはできません。

{{% /alert %}} 
###### **このセクションには、次のトピックが含まれています。**
- [テーブル アイテムの作成](/cells/ja/reportingservices/creating-table-item/)
- [サブレポートアイテムを追加](/cells/ja/reportingservices/add-sub-report-item/)
