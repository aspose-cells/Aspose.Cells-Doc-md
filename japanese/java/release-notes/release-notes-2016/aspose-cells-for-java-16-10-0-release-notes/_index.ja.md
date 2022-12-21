---
title: Aspose.Cells for Java 16.10.0 リリースノート
type: docs
weight: 30
url: /ja/java/aspose-cells-for-java-16-10-0-release-notes/
---
## **1) Aspose.Cells**

|**鍵** |**概要** |**カテゴリー** |
|:- |:- |:- |
|CELLSJAVA-41974 |レンダリングされた PDF ファイルでピボットテーブルの更新が機能しない|バグ|
|CELLSJAVA-41900 |XLSM は、単純なロードおよび保存操作によって破損する|バグ|
|CELLSJAVA-41790 |スプレッドシートを HTML に変換した後、ハイパーリンクが期待どおりに機能しない|バグ|
|CELLSJAVA-42010 |出力 PDF で一部の文字がレンダリングされない|バグ|
|CELLSJAVA-41977 |チャートの PDF で変更されたチャートの凡例の順序|バグ|
|CELLSJAVA-41972 |PDF で高低線の Z オーダーが正しくない|バグ|
|CELLSJAVA-42015 |Aspose.Cells で再保存するとスプレッドシートが破損する|バグ|
|CELLSJAVA-42005 |セルに挿入した後に数式が変更される|バグ|
|CELLSJAVA-41997 |スマート マーカーを使用した単純な Bean での奇妙な動作|バグ|
|CELLSJAVA-41993 |a7.xlsm ファイルを開く際の NullPointerException|例外|
|CELLSJAVA-41992 |a6.xlsm ファイルを開く際の NullPointerException|例外|
|CELLSJAVA-41991 |a5.xlsm ファイルを開く際の NullPointerException|例外|
|CELLSJAVA-41990 | a4.xlsm ファイルを開く際の NullPointerException|例外|
|CELLSJAVA-41989 | a3.xlsm ファイルを開く際の NullPointerException|例外|
|CELLSJAVA-41988 | a2.xlsm ファイルを開く際の NullPointerException|例外|
|CELLSJAVA-41987 | a1.xlsm ファイルを開く際の NullPointerException|例外|
|CELLSJAVA-41968 | IndexOutOfBoundsException: インデックス: 23、サイズ: 14 ピボットグラフの更新中|例外|
|CELLSJAVA-42014 |ClassCastException: XLSX の再保存中に com.aspose.cells.zadp を com.aspose.cells.zadq にキャストできない|例外|
## **Public API および下位互換性のない変更**
以下は、Aspose.Cells for Java に対して行われた下位互換性のない変更と同様に、追加、名前変更、削除、または廃止されたメンバーなど、パブリック API に対して行われた変更のリストです。リストされている変更について懸念がある場合は、 Aspose.Cells サポート フォーラム。
### **Shape.Reflection プロパティと ReflectionEffect クラスを追加**
グラフ要素または図形の反射効果を表します。
### **Shape.Glow、GlowEffect.Size、および GlowEffect.Transparency プロパティを追加**
グラフ要素または図形のグロー効果を表します。
### **LightRigType.None 列挙型を追加します**
照明設定なしを表します。
### **Shape.ShadowEffect プロパティを追加**
グラフ要素または図形の影の効果を表します。
### **ExternalLink.IsVisible プロパティを追加します**
外部リンクが表示されるかどうかを示します。
### **Shape.ThreeDFormat プロパティと ThreeDFormat クラスを追加**
形状の 3D 形式を取得および設定します。
### **PresetCameraType 列挙型を追加します**
位置を含むすべてのカメラ プロパティを設定するためのさまざまなアルゴリズム メソッドを表します。
### **LightRigDirectionType 列挙型を追加します**
ライト リグの方向タイプを表します。
### **BevelType 列挙型を追加します**
3D の形状に適用できるベベル タイプのプリセットを表します。
### **XmlMapCollection.Add(string url) メソッドを追加します**
XML ファイルの URL/パスによって XmlMap を追加します。
### **ShapeCollection.AddWordArt() メソッドと PresetWordArtStyle 列挙型を追加**
MS Excel 2007 以降のプリセット ワードアートを追加します。
### **FontSettingCollection.SetWordArtStyle() メソッドと FontSetting.SetWordArtStyle() メソッドを追加**
プリセットのワードアート スタイルを図形のテキストに設定します。
### **Cells.LinkToXmlMap(string mapName, int row, int column, string path) メソッドを追加**
xml マップにリンクします。
### **ListColumn.Formula プロパティを追加します**
リスト列の数式を取得および設定します。
### **GridWeb.CustomCalculationEngine プロパティと GridAbstractCalculationEngine クラスを追加**
Aspose.Cells.GridWeb の既定の計算エンジンを拡張するためのユーザーのカスタム計算エンジンを表します。
