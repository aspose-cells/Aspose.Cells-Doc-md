---
title: Open Save CancelダイアログなしでExcelファイルを開く Node.jsとC++を利用した方法
linktitle: 開く保存キャンセルダイアログボックスを表示せずにExcelファイルを開く
type: docs
weight: 150
url: /ja/nodejs-cpp/opening-excel-file-without-open-save-cancel-dialog-box/
--- 

{{% alert color="primary" %}} 

このドキュメントでは、Open-Save-Cancelダイアログボックスを表示せずにMicrosoft Excelファイルをブラウザで開く方法について説明しています。 

ここで注目すべきは、ファイルの直接ダウンロードを許可しないセキュリティ制約は、AsposeではなくMicrosoft（または他のブラウザベンダ）によって強制されるものです。これは、潜在的に有害なファイルをローカルマシンにダウンロードすることをブロックおよび制限するために課されています。 

クライアントのローカルシステムがOpen-Save-Cancelダイアログを表示せずにダウンロードを許可することはリスクが伴います。これは大きなセキュリティリスクとなるため、Asposeからはオプションや回避策は利用できません。

{{% /alert %}} 

## **なぜセキュリティリスクか？**
Internet Explorer がファイルをダウンロードしようとするときに表示される Open-Save-Cancel ダイアログボックスを示す以下の画像を参照してください。

|**Open-Save-Cancel ダイアログ**| 
| :- | 
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_1.png)| 
前述の通り、確認なしでファイルを開いたり実行したりできることはセキュリティリスクです。マルウェアやウイルスを含むファイルもあり、危険なファイルを無警告でダウンロードさせたり、ソースを確認せずに実行させたりするサイトもあります。そのため、ダウンロードのプロンプトを省略せずに、ユーザーがファイルとその出所を検証できるようにすることを推奨します。ダウンロードダイアログを無効にすると、システムはウイルス、トロイの木馬、ハッカーによる潜在的な攻撃に脆弱になります。 

## **Open-Save-Cancel ダイアログボックスを使用せずにファイルを開く**
セキュリティ上の大きな懸念事項であるにも関わらず、Microsoft はユーザーがファイルダウンロードの際に Open-Save-Cancel プロンプトを無効にするための Internet Explorer 設定を提供しています。 

Windows エクスプローラで:

1. **ツール** メニューから **フォルダオプション** を選択します。
1. フォルダオプションダイアログの **ファイルの種類** タブをクリックします。
1. XLS 拡張子のファイルタイプを選択します。
1. **高度** をクリックします。 
   ダイアログボックスが表示されます。下部に 3 つのオプションがあります。
1. **ダウンロード後に開くことを確認する** のチェックを外します。
1. 3 番目のオプション (**同じウィンドウ内で参照**) を選択し、Excel ファイルを Internet Explorer で単独の Microsoft Excel を起動せずに表示します。 

|**ファイルタイプオプションの編集**| 
| :- | 
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_2.png)| 
この設定により、ファイルを直接ウェブブラウザで実行できるようになり、ファイルをダウンロードまたは開く際に Open-Save-Cancel ダイアログが表示されることなく実行できます。 
{{< app/cells/assistant language="nodejs-cpp" >}}
