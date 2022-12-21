---
title: Aspose.Cells 7.0.0 以降に移行する方法
type: docs
weight: 10
url: /ja/java/how-to-migrate-to-aspose-cells-7-0-0-or-higher/
---
{{% alert color="primary" %}}

この記事では、Aspose.Cells for Java の前のバージョンと比較して、Aspose.Cells for Java 7.0.0 以降のバージョンで行われた API の注目すべき変更点を共有しました。この記事は、ユーザーが古い API から新しいバージョンにすばやく移行するのに役立ちます。 API 変更内容を理解し、アプリケーションで実行します。

{{% /alert %}}

## **既存ユーザー向けの主な変更点**

Aspose.Cells for Java v7.0.0 のリリース以降、API に大幅な変更を加え、現在までに Aspose.Cells for .NET に存在するすべての機能を追加しました。したがって、Aspose.Cells for Java と .NET の両方は、機能に関して、さらにはメソッドとプロパティ名に関しても同等になります。

古いアプローチと同様に、アプリケーションに import ステートメントを 1 つだけインポートして、すべてのクラス、インターフェースなどを取得できます。

[**Java**]{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}

特定の API のセットの名前を変更して、Aspose.Cells for .NET と一致するように API 構造を消去しました。いくつかのコレクション クラスを追加し、既存のコレクション クラスに置き換えました。 Like Worksheets クラスは次のように置き換えられました**ワークシート コレクション**.同様に、 Shapes クラスは次のように置き換えられました**シェイプコレクション**.ただし、クラスの機能は影響を受けず、強化されています。

新しい API に移行する場合は、アプリケーションで次の変更を実行して、最終的に機能させる必要がある場合があります。次のリストには、クラスとそれぞれのメソッドで行われた変更も含まれています。

## **APIの変更点のまとめ**

1) v2.5.4 以前の名前が「s」で終わるコレクションの名前が変更されました。 v7.0.0 以降では、コレクションは次のように命名されます。
例: Shapes (旧) -> ShapeCollection (新)、Worksheets (旧) -> WorksheetCollection (新)、など。

2) Collection からの要素の取得が変更されました。たとえば、v2.5.4 以前では getXXX(int) として実行していましたが、v7.0.0 以降では get(int) として実行します。
例: Worksheets.getSheet(int) (旧) -> WorksheetCollection.get(int) (新) など。

3) 1つのコレクションの取得サイズ(要素数)を変更。 v2.5.4 以前では size() で行っていましたが、v7.0.0 以降では getCount() で行います。
Worksheets.size() (旧) -> WorksheetCollection.getCount() (新) など。

4) v2.5.4 以前のブール型プロパティの getter メソッドのうち、「is」で始まる名前が変更されました。 v7.0.0 では、これらは「get」で開始されます。
例: PageSetup.isBlackAndWhite() (旧) -> PageSetup.getBlackAndWhite() (新) など。
