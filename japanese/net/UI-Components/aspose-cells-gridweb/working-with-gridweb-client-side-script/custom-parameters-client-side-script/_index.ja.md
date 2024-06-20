---
title: 初期化パラメータをカスタマイズする
type: docs
weight: 10
url: /ja/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
keywords: GridWeb、カスタマイズ、初期化パラメータのカスタマイズ
description: Aspose.Cells.GridWebのクライアント側スクリプトで初期化パラメータをカスタマイズする方法について紹介します。
---

{{% alert color="primary" %}} 

開発者はacwmain.jsでAspose.Cells.GridWebコントロールの動作をカスタマイズするために、異なる初期化パラメータ値を設定できます。  

{{% /alert %}} 

### **パラメータ**

|**パラメータ**|**説明**|
| :- | :- |
|needInitAlignmentAdjust| 初期化時にセルコンテンツの垂直配置を行うかどうか、大きなセルがある場合、パフォーマンスが低下する可能性があります。垂直配置に注意がない場合はfalseに設定できます。デフォルト値はtrueです。
|focusinside| セルスパン内にフォーカスを当てるかどうか、デフォルト値はtrueです。
|copy_with_style| スタイルをコピーするかどうか、デフォルト値はfalseで、セルコンテンツのみをコピーします。
|useESCAsLeave| [esc]キーを押した時のデフォルト動作は、セルの編集操作をキャンセルすることです。この値をtrueに設定すると、以前の値に変更せずにセルを離れるためのショートキーとして扱います。
|needValidateall| バリデーションを行う際にアクティブなワークシート上のすべてのバリデーションをバリデーションするかどうか、デフォルト値はfalseです。
|scrollToInvalidate| needValidateallがtrueの場合、最初の無効なセルを表示してスクロールするかどうか、デフォルト値はtrueです。


コード例の出力は以下のとおりです。[サンプルエクセルファイル](valign.xlsx)をご確認ください。

**needInitAlignmentAdjust=true** 

![todo:image_alt_text](align_true.png)

**needInitAlignmentAdjust=false** 

![todo:image_alt_text](align_false.png)

**focusinside=true** 
inside edit way -- テキストを入力する際、古いセルの値が保持されます。   

![todo:image_alt_text](focus_inside_true.png)

**focusinside=false** 
fast edit way -- テキストを入力する際、古いセルの値が上書きされます。古いセル値を基に編集する場合は、セルをクリックできます。

![todo:image_alt_text](focus_inside_false.png)



