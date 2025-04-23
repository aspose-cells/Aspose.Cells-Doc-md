---
title: 使用Kotlin读写Excel
type: docs
weight: 189
url: /zh/java/read-and-write-to-excel-with-kotlin/
description: 学习使用Aspose.Cells for Java在Kotlin中读取、写入和格式化Excel文件。包括公式和格式化的代码示例。
keywords: Kotlin Excel，Aspose.Cells Kotlin，阅读Excel Kotlin，写入Excel Kotlin，Excel公式Kotlin，Excel单元格格式，Aspose.Cells设置。
---

Aspose.Cells for Java是一个强大的库，允许开发人员以编程方式操作Excel文件。虽然它为Java设计，但由于Kotlin与Java的完全互操作性，将其无缝集成到Kotlin中。本指南提供了使用Kotlin和Aspose.Cells for Java读取和写入Excel文件的逐步指导。

## 先决条件
- 安装了Kotlin和Java开发工具包（JDK）。
- 配置依赖管理的构建工具（Maven或Gradle）。

## 在Kotlin项目中设置Aspose.Cells

将Aspose.Cells依赖项添加到你的项目中：

### 对于Maven（`pom.xml`）：
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
### 对于Gradle（`build.gradle.kts`）：
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
## 写入Excel

此示例演示如何创建一个新的Excel工作簿，填充单元格数据，并将文件保存到磁盘。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-WriteToExcel.kt" >}}

## 从Excel读取

此示例演示如何加载现有的Excel文件，读取单元格值，并打印结果。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-ReadFromExcel.kt" >}}

## 高级操作

### 处理公式

此示例向单元格添加了一个公式（`SUM`），重新计算了工作簿，并打印了结果。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-HandleFormulas.kt" >}}

### 格式化单元格

此示例对单元格应用了样式（加粗、红色、居中对齐）。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-FormatCells.kt" >}}

{{< app/cells/assistant language="java" >}}
