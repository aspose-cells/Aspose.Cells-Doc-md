---
title: Goコマンドを使用してAspose.Cells for Go via C++をインストールする方法について。
type: docs
linktitle: Goコマンドによるインストール
weight: 40
url: /ja/go-cpp/how-to-install-aspose-cells-for-go-via-c++-using-the-go-command
---


## **Goコマンドを使用したAspose.Cells for Go via C++のインストール方法**

   Go 1.16以降では、`go install`コマンドを直接使用してAspose.Cells for Go via C++パッケージをインストールできます。このコマンドは、既存のプロジェクト依存関係に影響を与えずにコマンドラインツールをグローバルにインストールできます。

```go

go install github.com/aspose-cells/aspose-cells-go-cpp/v25@latest

```

   `go get`コマンドを使用してAspose.Cells for Go via C++パッケージをインストールする場合、カレントディレクトリまたは親ディレクトリにgo.modファイルが存在している必要があります。[インストール方法とコードの実行についてはこちら](#Installation-in-your-project)

```go

go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1

```

### プロジェクトでのAspose.Cells for Go via C++パッケージのインストールとコード実行 {#Installation-in-your-project}

1. プロジェクトのディレクトリとmain.goファイルを作成し、次のコードを追加します。

```Go

package main

import (
 . "github.com/aspose-cells/aspose-cells-go-cpp/v25"
 "fmt"
)

func main() {
 lic, _ := NewLicense()
 lic.SetLicense_String("YOUR_LICENSE_File_PATH")
 workbook, _ := NewWorkbook()
 worksheets, _ := workbook.GetWorksheets()
 worksheet, _ := worksheets.Get_Int(0)
 cells, _ := worksheet.GetCells()
 cell, _ := cells.Get_String("A1")
 cell.PutValue_String_Bool("Hello World!", true)
 style, _ := cell.GetStyle()
 style.SetPattern(BackgroundType_Solid)
 color, _ := NewColor()
 color.Set_Color_R(uint8(255))
 color.Set_Color_G(uint8(128))
 style.SetForegroundColor(color)
 cell.SetStyle_Style(style)
 workbook.Save_String("HELLO.pdf")

}

```

1. プロジェクトのgo.modを初期化する

```bash

go mod init main

```

1. プロジェクトの依存関係を取得します。

```bash

go mod tidy

```

もし開発環境にAspose.Cells for Go via C++がインストールされていない場合、Goは自動的にパッケージを `$GOPATH` のサブディレクトリにインストールします。

1. 現在のコマンドシェルで共有ライブラリのパスを指すようにPATHを設定します。your_versionを実行中のAspose.Cells for Go via C++のバージョンに置き換えてください。

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1/lib/linux_x86_64/

```

またはPowerShellで

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.1\lib\win_x86_64\"

```

上記のパスからDLLファイルをコピーして、プロジェクトの実行ファイルと同じ場所に配置することもできます。

1. 作成したアプリケーションを実行します。

```bash

go run main.go

```
