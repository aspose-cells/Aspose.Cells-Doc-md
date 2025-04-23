---
title: はじめに
type: docs
weight: 10
url: /ja/go-cpp/getting-started/
description: C++経由でAspose Cells for Goをインストールし、Hello Worldアプリケーションを作成する方法。
---

{{% alert color="primary" %}}

このページでは、Aspose Cells for GoをC++経由でインストールし、Hello Worldアプリケーションを作成する方法を説明します。

{{% /alert %}}

## Aspose.Cells for Go via C++統合

Aspose.Cells for Go via C++へようこそ！このクロスプラットフォームソリューションは、WindowsとLinuxの両方をサポートします。開始するには、パッケージを使用したコードファイルを実行してください。

### 前提条件

- [Go（>=1.13）](https://golang.org/doc/install/)
- [Git](https://git-scm.com/downloads)

### プロジェクトでAspose.Cells for Go via C++を実行する

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
 workbook.Save_String("HELLO.xlsx")

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

1. 現在のコマンドシェルで共有ライブラリのパスを指すようにPATHを設定します。your_versionを実行中のAspose.Cells for Go via C++のバージョンに置き換えてください。

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.0/lib/linux_x86_64/

```

またはPowerShellで

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.0\lib\win_x86_64\"

```

上記のパスからDLLファイルをコピーして、プロジェクトの実行ファイルと同じ場所に配置することもできます。

1. 作成したアプリケーションを実行します。

```bash

go run main.go

```
