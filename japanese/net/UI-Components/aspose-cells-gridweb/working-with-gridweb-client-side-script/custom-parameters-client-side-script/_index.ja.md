---
title: 初期化パラメータのカスタマイズ
type: docs
weight: 10
url: /ja/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
description: Aspose.Cells.GridWeb クライアント側スクリプトで初期化パラメーターをカスタマイズする方法。
---
{{% alert color="primary" %}} 

開発者は、acwmain.js の Aspose.Cells.GridWeb コントロールに対して異なる動作を実行するために、異なる初期化パラメーター値を設定できます。

{{% /alert %}} 
 
### **パラメーター**
 
|**パラメータ**|**説明**|
|:- |:- |
|needInitAlignmentAdjust|初期化時にセル コンテンツの垂直方向の配置を行うかどうか、配置作業を行うのに時間がかかります。ワークシートに大きなセルがある場合、パフォーマンスが低下します。ユーザーが垂直方向の配置を気にしない場合、彼はそれを次のように設定できます。 false、デフォルト値は true|
|フォーカスインサイド|セル範囲内にフォーカスするかどうか。デフォルト値は true|
|コピー_と_スタイル|スタイル付きでコピーするかどうか。デフォルト値は false で、セルの内容のみをコピーすることを意味します|
|useESCAsLeave|esc を押したときのデフォルトの動作は、セルの編集操作のキャンセルとして機能します。この値を true に設定すると、以前の値に戻らずにセルを離れる短いキーとして扱われ、内部の編集方法も変更されます。編集方法を高速化するには、デフォルト値は false です|
|すべての検証が必要|検証を行うときに、アクティブ シートのすべての検証を検証するかどうか (aspx コントロール ページで ForceValidation="True" を設定)。デフォルト値は false|
|scrollToInvalidate|needValidateall が true に設定されている場合に、スクロールして最初の無効化セルを表示するかどうか。デフォルト値は true です。|
 
 
コード例の出力を以下に示します。[サンプルエクセルファイル](valign.xlsx):

**needInitAlignmentAdjust=true** 

![todo:画像_代替_文章](align_true.png)

**needInitAlignmentAdjust=false** 

![todo:画像_代替_文章](align_false.png)

**focusinside=真** 
内部編集方法 -- テキストを入力すると、古いセルの値が保持されます

![todo:画像_代替_文章](focus_inside_true.png)

**focusinside=false** 
高速編集方法 -- テキストを入力すると、古いセルの値が上書きされます。古いセルの値に基づいて編集する場合は、セルをクリックします。

![todo:画像_代替_文章](focus_inside_false.png)

 
 