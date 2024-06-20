---
title: データのフィルタリング
type: docs
weight: 100
url: /ja/net/aspose-cells-griddesktop/filtering-data/
keywords: GridDesktop,フィルタリング,データのフィルタリング,AutoFilter,RowFilterr
description: この記事では、GridDesktopのワークシートでデータをフィルタリングする方法について紹介します。
---

{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop**は、ユーザー向けに自動フィルターとカスタムデータフィルター機能を提供しています。これらの機能を使用すると、ワークシートから表示したいアイテムのみを選択する方法を見つけることができます。また、リスト内のアイテムを特定の基準に従ってフィルタリングすることができます。Auto-Filter / Custom Data Filter機能を使用して、テキスト、数字、または日付をフィルタリングすることができます。

**RowFilterSettings**クラスの**EnableAutoFilter**ブール属性を使用して、GridDesktopコントロールの自動フィルター機能を有効にすることができます。クラスの他のプロパティも使用できます。たとえば**HeaderRow**、**StartRow**、**EndRow**を使用して、見出し、開始行、終了行のインデックスを指定できます。**Criteria**プロパティは、カスタムフィルタリング基準を設定するために使用します。クラスには、指定された基準に基づいてフィルタリングされた行を取得するための**FilterRows**というメソッドもあります。

GridDesktopは「含む」タイプの検索（大文字と小文字を区別しない）属性もサポートしています。必要に応じて**GridColumn**クラスの**IgnoreCase**プロパティを使用して、大文字と小文字を区別するかどうかを指定できます。**GridColumn**クラスの**IsStartWithCriteria**というプロパティを使用して、RowFilterが列でStartWith基準を使用するかどうかを示すこともできます。プロパティのデフォルト値はfalseに設定されています。

{{% /alert %}} 
## **データのフィルタリング**
この例では、Auto-Filter およびカスタムデータフィルタの機能を実装しています。GridDesktop にいくつかのデータリストを記入し、Auto-Filter 機能を有効にしてから、特定の基準に基づいてフィルターされた行を検索します。
### **自動フィルタ**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **カスタムデータフィルタ**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
