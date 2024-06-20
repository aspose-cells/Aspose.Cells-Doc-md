---
title: システム要件
type: docs
weight: 30
url: /ja/cpp/system-requirements/
---

Aspose.Cells for C++は、Office AutomationまたはMicrosoft Excelアプリケーションを必要とせずに、C++開発者がプログラム的にスプレッドシートを作成、操作、および変換できるネイティブC++ライブラリです。

## サポートされているオペレーティングシステム

Aspose.Cells for C++は、次の64ビットまたは32ビットのオペレーティングシステムおよびプラットフォームをサポートしています。

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">オペレーティングシステム</td>
			<td style="font-weight: bold; width:400px">バージョン</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
			<td><ul><li>Windows x86</li><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
			<td>Linux</td>
			<td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04以降</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---><li>ARM向けLinux（aarch64）</li></ul></td>
		</tr>
  <tr>
			<td>macOS</td>
			<td><ul><li>macOS 11以降（arm64、x86_64）</li></ul></td>
		</tr>
</table>

## 開発環境

Windows、Linux、またはmacOS向けのアプリケーションを開発する際に、Aspose.Cells for C++を使用できます。

### Windows

Aspose.Cells for C++は、[Microsoft Visual Studio v142 Platform Toolset](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160)をサポートする開発環境でアプリケーションを開発する際に使用できますが、以下の表にリストされている環境が明示的にサポートされています。

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">開発環境</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

### Linux

Aspose.Cells for C++は、C++11以上をサポートする開発環境でアプリケーションを開発するために使用できますが、次のコンパイラとツールが明示的にサポートされています:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">コンパイラ</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0以降</li></ul></td>
			</tr>
</table>

### Linux への追加依存関係
Aspose.Cells for C++ on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries both dynamic library and tool. Please install it before using:

1. Installing fontconfig on Ubuntu or Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installing fontconfig on Fedora or CentOs<br>
`sudo yum install fontconfig`

### macOS 
Aspose.Cells for C++は、以下の開発環境でアプリケーションを開発するために使用できます:
* Xcode 12.5.1以降
* Clangとlibc++（Xcodeとデフォルトで提供されています）
