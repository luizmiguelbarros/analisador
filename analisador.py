import yt_dlp

def baixar_audio_yt_dlp(youtube_url, caminho_saida='audio'):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{caminho_saida}/audio.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print("Áudio baixado com sucesso!")

        return f"{caminho_saida}/audio.mp3"

    except Exception as e:
        print("Erro ao baixar o áudio:", e)
        return None

# Exemplo de uso
link = input("Cole o link do vídeo do YouTube: ")
baixar_audio_yt_dlp(link)

