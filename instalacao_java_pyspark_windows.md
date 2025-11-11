# Instalação do Java 11 para uso com PySpark no Windows

## Por que o Java é necessário para o PySpark?

O PySpark usa Python apenas como **interface de programação**.
O processamento real dos dados é feito pela **engine do Apache Spark**, que é desenvolvida em **Java e Scala**.

Por isso, mesmo quando escrevemos código em Python, o Spark precisa que exista um **JDK (Java Development Kit)** instalado na máquina para executar suas operações internas.

A versão recomendada para trabalhar com PySpark é o **Java 11**, pois versões mais novas (16, 17, 18, 21…) desativaram funções internas usadas pelo Spark.  
O JDK mais estável e amplamente utilizado hoje no ecossistema Big Data é o **Eclipse Temurin** (antigo AdoptOpenJDK), totalmente gratuito e open-source.

---

## 1) Verificando se você já possui Java instalado

Abra o Prompt de Comando (CMD) e execute:

```
java -version
```

### Se aparecer algo como:
openjdk version "11.0.xx"

* Você já está com Java 11 e pode pular para o passo 4.

### Se aparecer erro, versão 17, 18, 19, 20 ou versão corrompida:

* Você precisa remover a versão atual e instalar o Java 11.

---

## 2) Removendo versões antigas ou incompatíveis do Java

Abra o **PowerShell como Administrador** e execute:

```
wmic product where "name like 'Java%%'" call uninstall /nointeractive
```

Se existirem várias instalações, repita o comando até remover todas.

---

## 3) Instalando o Java 11 (recomendado pelo PySpark)

Abra o PowerShell (não precisa ser admin) e execute:

```
winget install EclipseAdoptium.Temurin.11.JDK --silent
```

Se você não tiver o `winget`, baixe manualmente:
https://adoptium.net/temurin/releases/?version=11

Escolha:
- Sistema: **Windows**
- Arquitetura: **x64**
- Pacote: **JDK**

Instale normalmente.

---

## 4) Configurando a variável de ambiente JAVA_HOME

### 4.1 Identifique a pasta do Java instalado
Normalmente será uma destas:

```
C:\Program Files\Eclipse Adoptium\jdk-11.0.x
```

### 4.2 Criando JAVA_HOME
1. Pressione `Win + R`
2. Digite `sysdm.cpl`
3. Vá em **Avançado → Variáveis de Ambiente**
4. Em *Variáveis do Sistema*, clique em **Novo**
   - Nome da variável:
     ```
     JAVA_HOME
     ```
   - Valor da variável (exemplo):
     ```
     C:\Program Files\Eclipse Adoptium\jdk-11.0.x
     ```

### 4.3 Adicionar ao PATH
Na mesma janela:
1. Selecione a variável `Path`
2. Clique em **Editar → Novo**
3. Adicione:

```
%JAVA_HOME%\bin
```

Clique **OK** até fechar todas as janelas.

---

## 5) Verificando se tudo está correto

Abra um novo terminal e execute:

```
java -version
```

Você deve ver:

```
openjdk version "11.0.xx"
```

Se aparecer isso: ✅ Java configurado corretamente.

---

## 6) Por que o PySpark precisa do Java?

O código do Spark é escrito em **Scala e Java**.  
Quando usamos PySpark, o Python **não processa os dados diretamente**.

Em vez disso:
| Componente | Linguagem | Função |
|-----------|-----------|--------|
| Seu Código | Python | Define a análise |
| PySpark API | Python → Java | Traduz operações |
| Engine Spark | Scala/Java | Executa e processa os dados |

Ou seja: **PySpark = Python + Engine Spark (Java)**.

---

## 7) Observação importante para quem usa WSL (Linux no Windows)

Se estiver usando PySpark dentro do WSL (Ubuntu, Debian, etc.), instale o Java lá também:

```
sudo apt update
sudo apt install openjdk-11-jdk -y
```

Se tiver múltiplas versões de Java no WSL, selecione a correta:

```
sudo update-alternatives --config java
```

Escolha a versão **11**.

---

## Conclusão

Após instalar e configurar o Java 11 corretamente:

- O erro `Java gateway process exited before sending its port number` desaparece.
- O PySpark inicia normalmente.
- Você pode executar seus scripts com:

```
python atividade.py
```
---

**Documento criado para suporte didático.**