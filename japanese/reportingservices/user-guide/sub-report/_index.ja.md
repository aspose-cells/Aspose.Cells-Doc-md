---
title: サブレポート
type: docs
weight: 90
url: /ja/reportingservices/sub-report/
---

{{% alert color="primary" %}} 

サブレポートはテーブル項目に埋め込むことができます。フォーマットは：&=subreport{ReportName=あなたのレポート名; パラメーター1名 = パラメーター1の値; パラメーター2名 = パラメーター2の値; ...}

**レポート定義内のサブレポート** 

![todo:image_alt_text](sub-report_1.png)

この例では、サブレポートの名前は“Sales Order Detail”です。1つのパラメーター、SalesOrderNumberを持っています。このパラメーターの値はEmpSalesDetail.SalesOrderNumberです。
### **サブレポートに関する制限事項**
1. サブレポートはAspose.Cells.ReportingServices Designerで設計する必要があります。
1. サブレポートはテーブルグループ行にのみ埋め込むことができ、グループ行にはサブレポート以外の要素を含めることはできません。サブレポートをテーブル詳細行やフッター行に埋め込むことはできません。
1. 現在、複数の階層にネストすることはサポートされていません。サブレポートには埋め込みレポートを含めることはできません。

{{% /alert %}} 
###### **このセクションには以下のトピックが含まれています:** 
- [テーブル項目の作成](/cells/ja/reportingservices/creating-table-item/)
- [サブレポート項目の追加](/cells/ja/reportingservices/add-sub-report-item/)
