---  
title: 複雑な基準を満たすレコードを表示するためにMicrosoft Excelの高度なフィルタを適用する方法
type: docs  
weight: 280  
url: /ja/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/  
description: Microsoft Excelの高度なフィルターを使用して複雑な条件を満たすレコードを表示する方法について、Aspose.Cells for Node.js via C++ APIを使って学びます。  
keywords: C++経由でNode.jsの高度なフィルターを適用、設定、追加、作成する方法。範囲に高度なフィルターを追加する方法も解説。  
---  

## **可能な使用シナリオ**  

Microsoft Excelでは、複合条件を満たすレコードを表示するためにワークシートデータに *高度なフィルター* を適用できます。Excelの *データ > 詳細設定* コマンドを使ってこのフィルターを適用することができます（スクリーンショット参照）。  

![todo:image_alt_text](1.png)  

Aspose.Cells for Node.js via C++は、[**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-) 方法を用いて高度なフィルターを適用することもできます。Microsoft Excelと同様に、以下のパラメータを受け付けます。  

**isFilter**  

リストをその場でフィルタ処理するかどうかを示します。  

**listRange**  

リストの範囲。  

**criteriaRange**  

基準の範囲。  

**copyTo**  

データをコピーする範囲。  

**uniqueRecordOnly**  

唯一の行を表示またはコピーします。  

## **複雑な基準を満たすレコードを表示するMicrosoft Excelの高度なフィルタの適用**  

次のサンプルコードは、[サンプルExcelファイル](48496692.xlsx)に高度なフィルターを適用し、[出力Excelファイル](48496691.xlsx)を生成します。スクリーンショットは両方のファイルを比較表示しています。スクリーンショット内のデータは、複雑な条件に従ってフィルタリングされています。  

![todo:image_alt_text](2.png)  

## **サンプルコード**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-AdvancedFilter.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
