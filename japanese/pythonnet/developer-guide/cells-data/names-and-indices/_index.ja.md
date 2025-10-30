---
title: セル名と行/列インデックスの変換
linktitle: セル名とインデックス変換
type: docs
weight: 10
url: /ja/python-net/names-and-indices/
description: Aspose.Cells for Python via .NET APIを介して、セル名と行/列インデックスの変換方法を学びます。
keywords: Python Excelライブラリ、行および列インデックスからセル名を取得するPython、セル名から行および列インデックスを取得するPython、安全なワークシート名を作成するPython、安全なワークシート名を追加するPython
---

## **行と列のインデックスからセル名を取得**
行と列のインデックスを指定すると、セルの名前を見つけることが可能です。 この記事では、その方法について説明します。
Aspose.Cells for Python via .NETは、開発者が行と列のインデックスを指定した場合にセルの名前を取得できる[**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int)メソッドを提供しています。

{{% alert color="primary" %}} 

Microsoft Excelとは異なり、Aspose.Cells for Python via .NETでは行と列のインデックスが1からではなく、0から始まります。

{{% /alert %}} 

次のサンプルコードは、既知の行と列インデックスを使用してセルの名前にアクセスするために[**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int)を使用する方法を示しています。コードにより、次の出力が生成されます。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-IndexToName-1.py" >}}

## **セル名から行と列のインデックスを取得**
セルの名前から行と列のインデックスを見つけることが可能です。 この記事では、その方法について説明します。
Aspose.Cells for Python via .NETは、開発者がセルの名前から行と列のインデックスを取得できる[**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)メソッドを提供しています。

{{% alert color="primary" %}} 

Microsoft Excelとは異なり、Aspose.Cells for Python via .NETでは行と列のインデックスが1からではなく、0から始まります。

{{% /alert %}} 

次のサンプルコードは、[**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)を使用してセルの名前から行と列インデックスを取得する方法を示しています。コードにより、次の出力が生成されます。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-NameToIndex-1.py" >}}

## **安全なシート名を作成します。**
ランタイムでシート名を割り当てる必要がある場合があります。このシナリオでは、<>()+?"といった追加の文字を含むシート名が存在する場合があります。シート名として許可されていない文字はユーザーが提供した事前の文字で置き換える必要があります。同様に、長さが31文字を超える場合もあるため、縮小する必要があります。Apache POIは安全な名前の作成の特定の機能を提供していますが、同様の機能をAspose.Cells for Python via .NETによって提供されており、これによりこれらの問題を処理するための機能が提供されています。次のサンプルコードは、この機能を示しています。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-CreateSafeSheetNames.py" >}}

出力:

これは最初の名前です。

` <> + (形容詞Private _ " Private"
{{< app/cells/assistant language="python-net" >}}
