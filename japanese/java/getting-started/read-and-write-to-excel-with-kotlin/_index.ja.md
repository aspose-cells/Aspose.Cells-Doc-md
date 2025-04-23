---
title: KotlinでExcelの読み書き
type: docs
weight: 189
url: /ja/java/read-and-write-to-excel-with-kotlin/
description: Kotlinを使ってExcelファイルの読み書きや書式設定を学び、Aspose.Cells for Javaを使用します。数式や書式設定のコード例も含まれています。
keywords: Kotlin Excel、Aspose.Cells Kotlin、KotlinでExcelを読む、KotlinでExcelを書き込む、Excel数式Kotlin、Excelセルの書式設定、Aspose.Cellsのセットアップ。
---

Aspose.Cells for Javaは、開発者がExcelファイルをプログラムmaticallyに操作できる強力なライブラリです。Java向けに設計されていますが、Kotlinと完全な相互運用性があるため、Kotlinにもシームレスに統合されます。このドキュメントは、KotlinとAspose.Cells for Javaを使用したExcelファイルの読み書きのステップバイステップガイドを提供します。

## 前提条件
- KotlinとJava開発キット（JDK）がインストールされています。
- 依存関係管理のためのビルドツール（MavenまたはGradle）が設定されています。

## KotlinプロジェクトにAspose.Cellsを設定する

プロジェクトにAspose.Cellsの依存関係を追加してください：

### Maven（`pom.xml`）の場合：
```xml
<repositories>
    <repository>
        <id>AsposeJavaAPI</id>
        <name>Aspose Java API</name>
        <url>https://releases.aspose.com/java/repo/</url>
    </repository>
</repositories>

<dependencies>
    <!-- Aspose.Cells for Java -->
    <dependency>
        <groupId>com.aspose</groupId>
        <artifactId>aspose-cells</artifactId>
        <version>25.2</version>
    </dependency>

    <!-- Mandatory Bouncy Castle Libraries -->
    <dependency>
        <groupId>org.bouncycastle</groupId>
        <artifactId>bcprov-jdk15on</artifactId>
        <version>1.68</version>
    </dependency>
    <dependency>
        <groupId>org.bouncycastle</groupId>
        <artifactId>bcpkix-jdk15on</artifactId>
        <version>1.68</version>
    </dependency>
</dependencies>
```
### Gradle（`build.gradle.kts`）の場合：
```kotlin
repositories {
    maven { url = uri("https://releases.aspose.com/java/repo/") }
}

dependencies {
    // Aspose.Cells for Java
    implementation("com.aspose:aspose-cells:25.2")

    // Mandatory Bouncy Castle Libraries
    implementation("org.bouncycastle:bcprov-jdk15on:1.68")
    implementation("org.bouncycastle:bcpkix-jdk15on:1.68")
}
```
## Excelに書き込む

この例は、新しいExcelワークブックを作成し、セルにデータを入力し、ファイルをディスクに保存する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-WriteToExcel.kt" >}}

## Excelから読み取る

この例は、既存のExcelファイルをロードし、セル値を読み取り、結果を印刷する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-ReadFromExcel.kt" >}}

## 高度な操作

### 数式の処理

この例では、セルに数式（`SUM`）を追加し、ワークブックを再計算し、結果を出力します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-HandleFormulas.kt" >}}

### セルの書式設定

この例では、セルにスタイリング（太字、赤色、中央揃え）を適用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-FormatCells.kt" >}}

{{< app/cells/assistant language="java" >}}
