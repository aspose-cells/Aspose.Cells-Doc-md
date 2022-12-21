---
title: コンポーネントのバージョン番号を確認する
type: docs
weight: 70
url: /ja/java/check-version-number-of-the-component/
---
{{% alert color="primary" %}} 

場合によっては、使用している製品のバージョンが不明な場合があります。多くの場合、新しい修正 (指摘されたユーザー シナリオのバグ修正) を作成し、緊急の必要性に反してフォーラムに投稿します。バージョン番号は、メジャー バージョン番号、マイナー バージョン番号、および修正プログラム バージョン番号で構成されます。定義されたすべてのコンポーネントは、0 以上の整数でなければなりません。バージョン番号の形式は次のとおりです。

major.minor.hotfix の場合、一部を 1 つ増やして新しいバージョンを作成する場合があります。通常、最後の部分を 1 増やして新しい修正を作成し、ユーザー向けのフォーラムに投稿します。

このドキュメントでは、システムにインストールされているコンポーネントのバージョンを確認するいくつかの方法について説明します。

{{% /alert %}} 
## **バージョン番号の確認**
### **1) 手動方法**
Java バージョン/修正プログラム (Aspose.Cells for Java) がある場合は、Aspose.Cells ライブラリ jar ファイルを解凍し、メモ帳で MANIFEST ファイルを開き、"Specification-Version: " という文字列を検索して、その値を確認します。

![todo:画像_代替_文章](check-version-number-of-the-component_1.png)


**形：** Java 修正のバージョン番号を確認する
### **2) API の使用**
次の API を使用して、製品のバージョン番号を取得することもできます。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

