from src.video import Video, PLVideo

if __name__ == '__main__':
    # Создаем два экземпляра класса
    video1 = Video('AWX4JnAnjBE')  # 'AWX4JnAnjBE' - это id видео из ютуб
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'

    # video1.print_vid_data()
    # video2.print_vid_data()
    # assert video2.title == "MoscowPython Meetup 78 - вступление"
    # assert video2.url == 'https://wwww.youtube.com/4fObz_qw9u4'
    # assert video2.view_count == '606'
    # assert video2.like_count == '9'
