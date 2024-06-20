---
title: コンポーネントのバージョン番号を確認する
type: docs
weight: 70
url: /ja/java/check-version-number-of-the-component/
---

{{% alert color="primary" %}} 

場合によっては、製品のバージョンを知りたいことがあります。多くの場合、新しい修正 (ユーザーシナリオのバグ修正) をビルドし、それをフォーラムに投稿して緊急に必要な場合があります。バージョン番号は、メジャー バージョン番号、マイナー バージョン番号、およびホットフィックス バージョン番号で構成されます。すべての定義済みコンポーネントは、0 以上の整数でなければなりません。バージョン番号の形式は次のとおりです:

major.minor.hotfix 、1 つの部分を 1 つ増やして新しいバージョンを作成する場合があります。通常、最後の部分を 1 つ増やして新しい修正をビルドし、フォーラムに投稿してユーザーに提供します。

このドキュメントでは、システムにインストールされているコンポーネントのバージョンを確認するいくつかの方法について説明します。

{{% /alert %}} 
## **バージョン番号の確認**
### **1) 手動による方法**
Java バージョン/修正 (Aspose.Cells for Java) を持っている場合、Aspose.Cells ライブラリ jar ファイルを展開し、MANIFEST ファイルをメモ帳で開き、"Specification-Version:" の文字列を検索してその値を確認できます。

![todo:image_alt_text](check-version-number-of-the-component_1.png)


**図:** Javaの修正のバージョン番号を確認する
### **2) APIを使用する**
製品のバージョン番号を取得するために以下のAPIを使用することもできます。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

