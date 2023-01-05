---
title: データのフィルタリング
type: docs
weight: 100
url: /ja/net/filtering-data/
---
{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop**ユーザーにオートフィルターとカスタムデータフィルター機能を提供します。これらの機能を使用すると、ワークシートからリストに表示する項目のみを選択する方法が見つかる場合があります。さらに、設定された基準に従ってリスト内のアイテムをフィルタリングすることができます。 Auto-Filter / Custom Data Filter 機能を使用して、テキスト、数値、または日付をフィルタリングできます。

使用できます**オートフィルターを有効にする**のブール属性**行フィルター設定**クラスを使用して、GridDesktop コントロールのオートフィルター機能を有効にします。使用できるクラスの他のプロパティがいくつかあります。**ヘッダー行** , **開始行**と**行末**ヘッダー、開始および終了行インデックスを指定します。の**基準**プロパティは、カスタム フィルタリング基準を設定するために使用されます。クラスには、という名前のメソッドもあります**FilterRows**指定された基準に基づいてフィルタリングされた行を取得します。

 RowFilter の「contains」タイプの検索 (大文字と小文字を区別しない) 属性は、GridDesktop でもサポートされています。あなたは使用することができます**大文字と小文字を区別しない**のプロパティ**グリッド列**クラスを使用して、必要に応じて大文字と小文字を区別する属性を指定します。という名前のプロパティを使用することもできます**IsStartWithCriteria**の**グリッド列** RowFilter が列で StartWith 基準を使用するかどうかを示すクラス。プロパティのデフォルト値は false に設定されています。

{{% /alert %}} 
## **データのフィルタリング**
この例では、オートフィルター機能とカスタム データ フィルター機能の両方を実装しています。 GridDesktop にいくつかのデータ リストを入力し、オート フィルター機能を有効にしてから、いくつかの基準に基づいてフィルター処理された行を検索します。
### **オートフィルター**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **カスタム データ フィルタ**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
