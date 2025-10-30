---  
title: Node.jsをC++経由で使用して印刷タイトルを設定する方法  
linktitle: 印刷タイトルの設定方法  
type: docs  
weight: 200  
url: /ja/nodejs-cpp/how-to-set-print-titles/  
description: この資料では、Node.jsとC++を使用してAspose.Cellsライブラリで印刷タイトルを設定する方法を説明します。  
keywords: 行と列を繰り返して印刷、Node.jsでの印刷タイトル設定、Node.jsを使用した印刷タイトルの設定とクリア、Node.jsでの印刷タイトルの追加と削除、Excelで印刷タイトルを設定する方法、Excelで印刷タイトルをクリアする方法。  
---  

## **可能な使用シナリオ**  

Excelで印刷タイトルを設定すると、特定の行または列がすべてのページで繰り返され、大きなスプレッドシートを複数ページにわたって印刷する場合に特に便利です。設定する理由は次の通りです：  

1. 読みやすさの向上：印刷タイトルは、見出しをすべてのページで表示し続けることで、データの理解を助けます。各ページで情報を解釈しやすくなります。  

1. 専門的な外観：各ページにヘッダーやラベルを一定して表示することで、印刷されたドキュメントに洗練されたプロフェッショナルな印象を与えます。  

1. ナビゲーションの改善：膨大なデータを含むドキュメントでは、各ページでヘッダーを繰り返すことで、迅速にナビゲートおよび参照でき、ページの行き来を減らすことができます。  

1. エラー低減：すべてのページにヘッダーがあると、誤解やデータ入力エラーの可能性が低減され、ユーザーがデータのコンテキストを簡単に理解できるためです。  

1. 一貫性：重要な情報（列見出しや行ラベルなど）が常に表示されることにより、ドキュメント全体の一貫性と明確さが保たれます。  

## **Excelで印刷タイトルを設定する方法**  

Excelで印刷タイトルを設定するには、次の手順に従います：  

1. ページレイアウトタブを開く：Excelウィンドウのリボンの「ページレイアウト」タブをクリックします。  
1. 印刷タイトルにアクセス： "ページ設定" グループ内の "印刷タイトル" をクリックします。  
1. 行の繰り返し設定： "ページ設定" ダイアログボックスの "シート" タブに移動します。 "印刷タイトル" セクションで、 "上部で繰り返す行" の横のボックスをクリックし、繰り返す行を選択します。  
1. 列の繰り返し設定（必要に応じて）：同様に、 "左側で繰り返す列" の横のボックスをクリックし、繰り返す列を選択します。  
<br>  
<img src="3.png" width=60% />  

1. 確認して印刷："OK" をクリックして設定を適用します。ワークシートを印刷すると、指定した行や列がすべてのページに表示されます。  

## **Excelで印刷タイトルをクリアする方法**  

Excelで印刷タイトルをクリアするには、繰り返す設定された行または列を削除する必要があります。次の手順です：  

1. ページレイアウトタブを開く：Excelウィンドウのリボンの「ページレイアウト」タブをクリックします。  
1. 印刷タイトルにアクセス： "ページ設定" グループ内の "印刷タイトル" をクリックします。  
1. 印刷タイトルをクリア：「ページ設定」ダイアログボックスの「シート」タブに移動します。「先頭行を繰り返す」および「左端列を繰り返す」のテキストボックス内の内容を削除してクリアします。  
<br>  
<img src="4.png" width=60% />  

1. 確認して閉じる：「OK」をクリックして変更を適用します。  

## **Aspose.Cells for Node.js via C++を使用した印刷タイトルの設定方法**  

指定したシートにプリントタイトルを設定するには、まず[サンプルファイル](input.xlsx)を読み込み、次に望むシートの[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/)オブジェクトの[**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--)と[**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--)のプロパティを変更します。これらのプロパティに範囲文字列を設定するとプリントタイトルが設定されます。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set rows to repeat at the top (e.g., rows 1 and 2)
worksheet.getPageSetup().setPrintTitleRows("$1:$2");

// Set columns to repeat at the left (e.g., columns A and B)
worksheet.getPageSetup().setPrintTitleColumns("$A:$B");

// Save the workbook
workbook.save("set_print_titles.pdf");
```  

出力結果：  
<br>  
<img src="1.png" width=60% />  

## **Aspose.Cells for Node.js via C++を使用した印刷タイトルのクリア方法**  

指定したシートのプリントタイトルをクリアするには、まず[サンプルファイル](input.xlsx)を読み込み、次に望むシートの[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/)オブジェクトの[**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--)と[**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--)のプロパティを変更します。これらのプロパティを空文字に設定するとプリントタイトルがクリアされます。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Clear the rows and columns set to repeat
worksheet.getPageSetup().setPrintTitleRows("");
worksheet.getPageSetup().setPrintTitleColumns("");

// Save the workbook
workbook.save("clear_print_titles.pdf");
```  

出力結果：  
<br>  
<img src="2.png" width=60% />  

{{< app/cells/assistant language="nodejs-cpp" >}}
