import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
export const Contact =() => {
  return (
    <Form>
      <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
        <Form.Label>Email</Form.Label>
        <Form.Control type="email" placeholder="vinsensius.120140192@student.itera.ac.id" />
      </Form.Group>
      <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
        <Form.Label>Isi Keluhan atau Saranmu Yukk</Form.Label>
        <Form.Control as="textarea" rows={3} />
      </Form.Group>
         <Form.Group controlId="formFileSm" className="mb-3">
        <Form.Label>Upload Bukti Keluhananmu Yukk</Form.Label>
        <Form.Control type="file" size="sm" />
      </Form.Group>
       <Button variant="secondary">Kirim</Button>{' '}
    </Form>
  );
}
