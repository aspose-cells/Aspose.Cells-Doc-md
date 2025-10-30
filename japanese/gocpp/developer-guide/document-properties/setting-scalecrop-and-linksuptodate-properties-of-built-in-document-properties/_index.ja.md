---
title: Golang経由のC++で組み込みドキュメントプロパティのScaleCropとLinksUpToDateプロパティを設定
linktitle: ScaleCropとLinksUpToDateプロパティの設定方法
type: docs
weight: 320
url: /ja/go-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Aspose.Cells for C++を使用して、組み込みドキュメントプロパティのScaleCropとLinksUpToDateの設定方法を学びます。
---

## **可能な使用シナリオ**
[GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/)および[GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/)は、OpenXml形式内に定義された2つの拡張組み込みドキュメントプロパティです。これらのプロパティの目的は次のとおりです。

## **1) ScaleCrop**
この要素は、ドキュメントサムネイルの表示モードを示します。この要素を**TRUE**に設定すると、ドキュメントサムネイルを表示に合わせてスケーリングします。この要素を**FALSE**に設定すると、ドキュメントサムネイルを表示に合わせてクロップします。

この要素の可能な値は、W3C XML Schema booleanデータ型で定義されています。

## **2) LinksUpToDate**
この要素は、ドキュメント内のハイパーリンクが最新であるかどうかを示します。この要素を**TRUE**に設定すると、ハイパーリンクが更新されていることを示します。この要素を**FALSE**に設定すると、ハイパーリンクが更新されていないことを示します。

この要素の可能な値は、W3C XML Schema booleanデータ型で定義されています。

## **これらのプロパティを示すスクリーンショット**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **組み込みドキュメントプロパティのScaleCropとLinksUpToDateの設定**
以下のサンプルコードは、ワークブックの拡張組み込みドキュメントプロパティである[GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/)と[GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/)を設定します。このコードで生成された[出力Excelファイル](5115500.xlsx)を確認し、拡張子を.zipに変更して内容を解凍し、上のスクリーンショットのようにapp.xmlを表示してください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingScalecropAndLinksuptodatePropertiesOfBuiltInDocumentProperties.go" >}}
