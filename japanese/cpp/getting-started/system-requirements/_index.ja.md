---
title: システム要求
type: docs
weight: 30
url: /ja/cpp/system-requirements/
---
Aspose.Cells for C++ は、C++ 開発者が Office オートメーションや Microsoft Excel アプリケーションを必要とせずにプログラムでスプレッドシートを作成、操作、変換できるようにするネイティブ C++ ライブラリです。

## サポートされているオペレーティング システム

Aspose.Cells for C++ は、次の 64 ビットまたは 32 ビットのオペレーティング システムとプラットフォームをサポートします。

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">オペレーティング·システム</td>
			<td style="font-weight: bold; width:400px">バージョン</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
			<td><ul><li>Windows x86</li><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
			<td>Linux</td>
			<td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 or later</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---><li>ARM 用 Linux (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>マックOS</td>
			<td><ul><li>macOS 11以降(arm64、x86_64)</li></ul></td>
		</tr>
</table>

## 開発環境

Windows、Linux、または macOS 用のアプリケーションを開発する場合は、Aspose.Cells for C++ を使用できます。

###  Windows

 Aspose.Cells for C++ は、サポートする開発環境でアプリケーションを開発するために使用できます。[Microsoft Visual Studio v142 プラットフォーム ツールセット](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160)ただし、次の表にリストされている環境は明示的にサポートされています。

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">開発環境</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

### Linux

Aspose.Cells for C++ は、C++11 以降をサポートする開発環境でアプリケーションを開発するために使用できますが、次のコンパイラとツールが明示的にサポートされています。

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">コンパイラ</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0以降</li></ul></td>
			</tr>
</table>

### Linux への追加の依存関係
Linux の Aspose.Cells for C++ は以下に依存します<a href="https://www.freedesktop.org/wiki/Software/fontconfig/">フォント設定</a>ダイナミック ライブラリとツールの両方のバイナリ。使用する前にインストールしてください:

1. Ubuntu または Debian への fontconfig のインストール<br>
`sudo apt install libfontconfig fontconfig`
1. Fedora または CentOs への fontconfig のインストール<br>
`sudo yum install fontconfig`

### マックOS
Aspose.Cells for C++ は、次の開発環境でアプリケーションを開発するために使用できます。
* Xcode 12.5.1以降
* Clang および libc++ (デフォルトで Xcode に同梱されています)
