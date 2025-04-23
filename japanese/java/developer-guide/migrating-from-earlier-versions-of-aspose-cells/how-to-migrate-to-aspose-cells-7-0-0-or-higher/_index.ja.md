---
title: Aspose.Cells 7.0.0以上への移行方法
type: docs
weight: 10
url: /ja/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---

{{% alert color="primary" %}}

この記事では、Aspose.Cells for Java 7.0.0以降のAPIで行われた注目すべき変更点を共有しています。以前のAPIから新しいAPIに迅速に移行するために、変更点を理解し、それをアプリケーションに反映させることでユーザーの移行を支援します。

{{% /alert %}}

## **既存ユーザー向けの注目すべき変更**

Aspose.Cells for Java v7.0.0のリリース以来、APIに大幅な修正を加え、現在までのAspose.Cells for .NETの機能をすべて追加しました。そのため、Aspose.Cells for Javaと.NETは機能面やメソッド・プロパティ名の点でも比較可能になりました。

古いアプローチと同様に、アプリケーションで1つだけのimportステートメントをインポートすることで、すべてのクラス、インタフェースなどを取得することができます。

[**Java**]

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}

API構造を整理して、Aspose.Cells for .NETと一致するようにAPIの一部の名前を変更しました。新たにいくつかのコレクションクラスを追加し、既存のコレクションクラスと置き換えました。たとえば、Worksheetsクラスは**WorksheetCollection**に置き換えられました。同様に、Shapesクラスは**ShapeCollection**に置き換えられました。ただし、クラスの機能は影響を受けずに向上しています。

新しいAPIに移行する場合、アプリケーションで以下の変更を行う必要があります。以下のリストには、クラスおよびそれに関連するメソッドで行われた変更が含まれています。

## **APIの変更点の概要**

1) v2.5.4以前のコレクションの名前が's'で終わるものはリネームされました。v7.0.0以降ではコレクションは次のように命名されます:
例：Shapes（旧）-> ShapeCollection（新）、Worksheets（旧）-> WorksheetCollection（新）、...等

2) コレクションから要素を取得する方法が変わりました。例えば、v2.5.4以前ではgetXXX(int)としていましたが、v7.0.0以降ではget(int)としています:
例：Worksheets.getSheet(int)（旧）-> WorksheetCollection.get(int)（新）、...等

3) 1つのコレクションの要素数を取得する方法が変わりました。v2.5.4以前ではsize()でしたが、v7.0.0以降ではgetCount()となりました:
Worksheets.size()（旧）-> WorksheetCollection.getCount()（新）、...等

4) v2.5.4以前のブール値プロパティのgetterメソッドは、'is'で始まるものが変更されています。v7.0.0ではこれらは"get"で始まります:
例：PageSetup.isBlackAndWhite()（旧）-> PageSetup.getBlackAndWhite()（新）、...等
{{< app/cells/assistant language="java" >}}
