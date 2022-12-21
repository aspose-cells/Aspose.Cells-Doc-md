---
title: Linux に TrueType フォントをインストールする方法
type: docs
weight: 20
url: /ja/java/how-to-install-truetype-fonts-on-linux/
---
{{% alert color="primary" %}}

最も可能性の高いシナリオは、スプレッドシートを PDF に変換するために Aspose.Cells を使用していることです。 Linux などの非 Windows ベースのオペレーティング システムでこれを実行している場合、このトピックでは、Aspose.Cells が最高の忠実度でスプレッドシートをレンダリングすることを確認する方法について説明します。

Aspose.Cells で変換されたスプレッドシートができるだけオリジナルに近く表示されるようにするには、Linux システムに「Windows フォント」または「TrueType フォント」をインストールする必要がある場合があります。これは、最も一般的に使用される TrueType フォントがプリインストールされていないためですデフォルトでは Linux ディストリビューション。

Linux システムで TrueType フォントを取得するには、主に 2 つの方法があります。

1. フォント ファイル (.TTF および .TTC) を Windows マシンから Linux マシンにコピーします。
1. msttcorefonts などの TrueType フォント パッケージをインストールします。

{{% /alert %}}

## **Windows マシンからフォントをコピーする**

簡単で迅速な方法は、Windows マシンの C:\Windows\Fonts ディレクトリから Linux マシンのディレクトリに .TTF および .TTC ファイルをコピーすることです。これらのフォントを Linux にインストールまたは登録する必要はありません。アプリケーションで FontConfigs.setFontFolder メソッドを使用してフォントの場所を指定するだけで済みます。

{{% alert color="primary" %}}

私たちの知る限り、Microsoft はフォントを誰でも自由に使用できるようにライセンスを供与していますが、フォントのライセンスについてはご自身でご確認ください。

{{% /alert %}}

## **TrueType フォント パッケージをインストールする**

以下に提供される情報は、Fedora や Red Hat Enterprise Linux (RHEL) などの Linux ディストリビューションに Microsoft の最も有名な TrueType フォントをインストールするための手順を順を追って説明します。

{{% alert color="primary" %}}

「root」レベルの権限が必要な場合があるため、「root」としてログインするか、sudo を設定してください。

{{% /alert %}}

ターミナルを使用してそれを行う方法は次のとおりです。

1. 次の RPM パッケージがインストールされていることを確認します。
   1. **rpm-ビルド**インストールされていない場合は、次のコマンドを使用して rpm-build パッケージをインストールします。

{{< highlight "java" >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**: インストールされていない場合は、次のコマンドを使用します

{{< highlight "java" >}}

yum \-y install wget

{{< /highlight >}}

1. 次のコマンドを使用して、SourceForge から最新の msttcorefonts 仕様ファイルをダウンロードします。

{{< highlight "java" >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. 以前にダウンロードしたスペック ファイルと次のコマンドを使用して RPM ファイルをビルドします。

{{< highlight "java" >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. RPM ファイルは /root/rpmbuild/RPMS/noarch/ に保存されます。次のようにインストールします。

{{< highlight "java" >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. マシンを再起動して、変更を有効にします。

上記の手順により、次のフォント ファミリを含む Microsoft TTF パッケージがインストールされます。

1. アンデール Mono
1. Arial 黒/Arial (太字、斜体、太字斜体)
1. Comic Sans MS (太字)
1. Courier New (太字、斜体、太字斜体)
1. ジョージア (太字、斜体、太字斜体)
1. 影響
1. タホマ
1. Times New Roman (太字、斜体、太字斜体)
1. トレビュシェット (太字、斜体、太字斜体)
1. Verdana (ボールド、イタリック、ボールド イタリック)
1. ウェッディング

{{% alert color="primary" %}}

Ubuntu では、Synaptic Package Manager に移動します。を見つけてインストールする**ttf-mscorefonts-インストーラー**パッケージ。

{{% /alert %}}
