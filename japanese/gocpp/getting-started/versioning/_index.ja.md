---
title: バージョニング
type: docs
weight: 40
url: /ja/go-cpp/versioning/
description: C++経由でAspose Cells for Goをインストールし、Hello Worldアプリケーションを作成する方法。
---

**github.com/aspose-cells/aspose-cells-go-cpp/v25**は、サードパーティライブラリの特定のバージョンを指定するGoモジュールパスです。このモジュールパスの意味を分解して説明します：
モジュールパスの分解

1. **GitHubリポジトリアドレス**：github.com/aspose-cells/aspose-cells-go-cpp

- この部分は、そのライブラリがGitHub上の、aspose-cells組織またはユーザーのリポジトリで、名前がaspose-cells-go-cppであることを示しています。
- Aspose.Cellsは、スプレッドシートファイル（Excelなど）を操作・処理するAPIのスイートです。

1. **バージョン番号**：/v25

- /v25は、このライブラリのバージョン24を示します。Go Modulesでは、セマンティックバージョニング（SemVer）がサポートされており、/vNを含むパスはメジャーバージョン番号を明示的に示すために使用されます。
- メジャーバージョンが2以上の場合、モジュールパスにバージョン番号を含める必要があり、互換性と異なるメジャーバージョン間の分離が確保されます。

### **意味合い**

- **aspose-cells-go-cpp**：これはC++ライブラリのGoバインディングで、Aspose.Cellsの機能をGoプログラム内で使用できるようにし、Excelファイルの読み取り、書き込み、操作などを可能にします。
- **v25**：これは、ライブラリのバージョン24を参照していることを示します。異なるメジャーバージョンでは互換性のない変更が導入される場合があるため、バージョン番号の指定は、正しいAPIと動作に依存させるために重要です。

### **使用例**

Goプロジェクトでaspose-cells-go-cpp v25を使用するには、次の行をgo.modファイルに追加してください：

```Go
require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.x.x
```

v25.x.xを特定のマイナーとパッチバージョン番号（例：v25.0.0）に置き換えます。この依存関係はgo getコマンドを使用して自動的に追加およびダウンロードできます：

```Go
go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.x.x
```
