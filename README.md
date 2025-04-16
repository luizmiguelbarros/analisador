# Analisador de Vídeos do YouTube com IA

Este é um projeto em Python que analisa vídeos do YouTube utilizando inteligência artificial.  
O objetivo é extrair o áudio de um vídeo, transcrevê-lo e classificar o tipo de conteúdo apresentado.

## Funcionalidades

- Entrada de link do YouTube
- Extração do áudio com `yt_dlp`
- Transcrição do áudio com `Whisper` (OpenAI)
- Classificação básica do tipo de conteúdo
- Saída exibida no terminal (VSCode)

## Requisitos

- Python 3.10 ou superior
- [yt_dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://ffmpeg.org/download.html) instalado e configurado no PATH
