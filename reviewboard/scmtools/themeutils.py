def handle_template_upload(file, path, prefix):
	destination = open(path + '/' + prefix + '_' + file, "wb+")
	for block in file.chunks():
		destination.write(block)
	destination.close()

