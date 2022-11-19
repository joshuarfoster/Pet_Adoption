from models import Pet, db
from app import app


with app.app_context():


    db.drop_all()
    db.create_all()


    Spike = Pet(name='Spike', species='porcupine', photo_url='https://th-thumbnailer.cdn-si-edu.com/qhn4f5uDwytUEKNehOauJNRLKTs=/1072x720/filters:no_upscale()/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer/ef/ff/efff9ae5-1832-489f-bb1f-f1a00944a8aa/hedgehog.jpg',age=2)
    Bubbles=Pet(name='Bubbles',species='cat',photo_url='https://www.bluevalleyanimalhospital.net/blog/wp-content/uploads/2019/08/iStock-495910314.jpg',age=1)
    Bojack=Pet(name='Bojack', species='dog',photo_url='https://media.npr.org/assets/img/2022/05/25/gettyimages-917452888-edit_custom-c656c35e4e40bf22799195af846379af6538810c-s1100-c50.jpg', notes = 'Likes sugar cubes')
    George=Pet(name='George', species='dog', photo_url='https://post.healthline.com/wp-content/uploads/2020/08/3180-Pug_green_grass-732x549-thumbnail-732x549.jpg')

    db.session.add(Spike)
    db.session.add(Bubbles)
    db.session.add(Bojack)
    db.session.add(George)

    db.session.commit()